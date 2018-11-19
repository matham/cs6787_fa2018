import numpy as np
from os.path import join, exists, dirname
import os
import re
import sys
import datetime
import cs6787
from collections import defaultdict
import torch
import torch.utils.data as data


class NoaaDataset(data.Dataset):

    root = ''

    header = []

    data = []

    x = []

    y = []

    stage_indices = []

    day = 0

    days = []

    total_size = 0

    def __init__(
            self, root, stage, predicted_features, data_split=(.8, .1, .1),
            split_fname='split.npz', include_invalid=False, epoch_days=0,
            warm_epoch_days=0, randomize_samples=False, rotate_data=False,
            **kwargs):
        super(NoaaDataset, self).__init__(**kwargs)
        self.root = root
        self.load_all_hourly_data()
        self.split_data(stage, data_split, split_fname)

        if randomize_samples:
            times = self.data[:, 0].copy()
            np.random.shuffle(times)
            self.data[:, 0] = times

        pred_indices = [self.header.index(name) for name in predicted_features]
        data_indices = [
            i for i in range(self.data.shape[1]) if i not in pred_indices]

        x = self.data[self.stage_indices, :][:, data_indices]
        y = self.data[self.stage_indices, :][:, pred_indices]

        if not include_invalid:
            valid = np.logical_not(
                np.logical_or(
                    np.any(x == -9999., axis=1), np.any(y == -9999., axis=1)))
            x = x[valid, :]
            y = y[valid, :]

        if epoch_days:
            times = x[:, 0]
            if rotate_data:
                max_ = np.max(times)
                min_ = np.min(times)
                center = (min_ + max_) / 2.
                times = np.where(times < center, times + (max_ - min_), times)
            self.compute_days(times, warm_epoch_days, epoch_days)

        self.total_size = x.shape[0]
        self.x = torch.from_numpy(x).float()
        self.y = torch.from_numpy(y).float()
        self.data = np.array([])  # release memory

    def __getitem__(self, index):
        if self.days:
            index = self.days[self.day][index]
        return self.x[index, 1:], self.y[index, :]

    def __len__(self):
        if self.days:
            return self.days[self.day].shape[0]
        return self.x.shape[0]

    def compute_days(self, times, warm_epoch_days, epoch_days):
        indices = np.argsort(times)
        dt = (datetime.datetime(year=1981, month=1, day=2) -
              datetime.datetime(year=1981, month=1, day=1)).total_seconds()

        i = 0
        t = np.min(times)
        end = t + dt * warm_epoch_days
        day_indices = []
        while i < len(times) and times[indices[i]] < end:
            day_indices.append(indices[i])
            i += 1
        days = self.days = [np.array(day_indices)]

        t += dt * warm_epoch_days
        dt *= epoch_days
        while i < len(times):
            day_indices = []
            end = t + dt
            while i < len(times) and times[indices[i]] < end:
                day_indices.append(indices[i])
                i += 1

            days.append(np.array(day_indices))
            t += dt

    def split_data(self, stage, data_split, split_fname):
        fname = join(dirname(cs6787.__file__), 'logs', split_fname)
        if not exists(fname):
            train, val, test = data_split
            mask_ = np.random.random((self.data.shape[0], ))

            mask = np.ones((self.data.shape[0], ), dtype=np.uint8) * 2
            mask[mask_ < train] = 0
            mask[np.logical_and(train <= mask_, mask_ < train + val)] = 1

            np.savez_compressed(fname, mask=mask)

        items = np.load(fname)['mask']
        indices = np.arange(len(items))
        stage = {'train': 0, 'val': 1, 'test': 2}[stage]
        self.stage_indices = indices[items == stage]

    def load_stations(self):
        col = 37
        station_pos = {}
        split_pat = re.compile(' +')
        with open(join(
                self.root, 'normals_1981-2010', 'hly-inventory.txt')) as fh:
            line = fh.readline()
            while line:
                station, a, b, c = re.split(split_pat, line[:col])
                station_pos[station] = float(a), float(b), float(c)
                line = fh.readline()
        return station_pos

    def create_data_rows(self, example_file, stations):
        data = []
        years = defaultdict(int)
        base_year = 1981
        t_start = datetime.datetime(year=1981, month=1, day=1)
        data_row_map = {}
        header = ['time', 'lat', 'long', 'elev']

        with open(join(
                self.root, 'normals_1981-2010', 'hourly', example_file)) as fh:
            line = fh.readline()
            while line:
                name = line[:11].strip()
                month = int(line[12:14].strip())
                day = int(line[15:17].strip())
                year = years[(name, month, day)] + base_year
                years[(name, month, day)] += 1

                for hour in range(24):
                    key = name, year, month, day, hour
                    data_row_map[key] = len(data)
                    item = []
                    data.append(item)

                    t = datetime.datetime(
                        year=year, month=month, day=day, hour=hour)
                    dt = (t - t_start).total_seconds()
                    item.append(dt)
                    item.extend(stations[name])

                line = fh.readline()

        return header, data, data_row_map

    def load_hourly_data(self, dataset_name, header, data, data_row_map):
        years = defaultdict(int)
        base_year = 1981
        bad_vals = {-9999., -8888., -7777., -6666., -5555.}
        bad_val = -9999.
        header.append(dataset_name.split('-', maxsplit=1)[1][:-4])

        with open(join(
                self.root, 'normals_1981-2010', 'hourly', dataset_name)) as fh:
            line = fh.readline()
            while line:
                name = line[:11].strip()
                month = int(line[12:14].strip())
                day = int(line[15:17].strip())
                year = years[(name, month, day)] + base_year
                years[(name, month, day)] += 1

                for hour, s in enumerate(range(18, 185, 7)):
                    val = float(line[s:s + 5].strip())
                    if val in bad_vals:
                        val = bad_val
                    flag = line[s + 5].strip()

                    key = name, year, month, day, hour
                    item = data[data_row_map[key]]
                    item.append(val)

                line = fh.readline()

    def load_all_hourly_data(self):
        npz = join(dirname(cs6787.__file__), 'data', 'hourly_data.npz')
        if exists(npz):
            data_dict = np.load(npz)
            self.header = data_dict['header'].tolist()
            self.data = data_dict['data']
            return

        stations = self.load_stations()
        files = list(
            os.listdir(join(self.root, 'normals_1981-2010', 'hourly')))
        header, data, data_row_map = self.create_data_rows(files[0], stations)

        for dataset_name in files:
            print('reading', dataset_name)
            self.load_hourly_data(dataset_name, header, data, data_row_map)

        lengths = {len(item) for item in data}
        assert len(lengths) == 1
        assert lengths.pop() == len(header)
        self.data = np.array(data)
        self.header = header

        np.savez_compressed(npz, data=self.data, header=self.header)


if __name__ == '__main__':
    loader = NoaaDataset(
        root=sys.argv[1], stage='train', predicted_features='temp-normal')
