import numpy as np
from os.path import join
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import csv
from collections import defaultdict
import os
from functools import partial

matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams['savefig.dpi'] = 300


def get_data(root, name):
    with open(join(root, name)) as fh:
        reader = csv.reader(fh)
        lines = list(reader)[2:]

        n = (len(lines[0]) - 1) / 3
        assert n.is_integer()
        n = int(n)

        data = np.array([list(map(float, line[n + 1: 2 * n + 1])) for line in lines])
        days = np.array([int(line[0]) for line in lines])
        for row in range(data.shape[0]):
            data[row, row + 1:] = 0
        return days, data


def show_daily_error(root, name):
    days, data = get_data(root, name)
    test_days = np.arange(data.shape[1])
    days = days[:, np.newaxis].repeat(len(test_days), 1)
    test_days = test_days[np.newaxis, :].repeat(data.shape[0], 0)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(
        days[:, :], test_days[:, :], data[:, :], cmap=cm.coolwarm, linewidth=0,
        antialiased=False)
    plt.xlabel('Day')
    plt.ylabel('Test days')
    plt.title('SGD Randomized')


def show_best_daily_error(root, start=0., mult=.01):
    files_ = [f for f in os.listdir(root) if f.startswith('day_test_log_full_')]
    times = [os.path.getmtime(join(root, f)) for f in files_]
    files_ = sorted(files_, key=lambda f: times[files_.index(f)])

    vals = []
    files = []
    cw = []
    i = 0
    for filename in files_:
        data = get_data(root, filename)[1]
        if np.isnan(data).any() or data.shape[0] != 35:
            print('skipping {}'.format(filename))
            i += 1
            continue

        max_val = data.max()
        vals.append(max_val)
        cw.append(i * mult + start)
        files.append(filename)
        i += 1

    vals = np.array(vals)
    cw = np.array(cw)
    i = np.argmin(vals)
    print('min max-error is "{}" for file "{}" at time "{}"'.format(vals[i], files[i], cw[i]))
    sort_i = np.argsort(vals)
    print(vals[sort_i])
    print([files[i] for i in sort_i])
    print(cw[sort_i])
    plt.plot(cw, vals)
    return files[i], cw, vals


def show_resample(root, label, color, func=np.max, rows=slice(None)):
    files = [f for f in os.listdir(root) if f.startswith('day_test_log_full_')]
    items = defaultdict(list)

    for filename in files:
        data = get_data(root, filename)[1]
        if np.isnan(data).any() or data.shape[0] != 35:
            print('skipping {}'.format(filename))
            continue
        n = int(filename[:-4].split('_')[-1])
        items[n].append(data)

    for n, vals in items.items():
        for val in vals:
            plt.plot([n], [func(val[rows, :])], '*' + color)

    labels = list(sorted(items.keys()))
    values = [None, ] * len(labels)
    for n, vals in items.items():
        values[labels.index(n)] = func(np.mean(np.array(vals), axis=0)[rows, :])
    plt.semilogx(labels, values, color, label=label)


def compare_baseline(root, val, baseline_val=0., func=np.max, rows=slice(None)):
    files = [f for f in os.listdir(root) if f.startswith('day_test_log_full_')]

    for filename in files:
        data = get_data(root, filename)[1]
        if np.isnan(data).any() or data.shape[0] != 35:
            print('skipping {}'.format(filename))
            continue

        if filename.endswith('False_0.csv'):
            c = 'r'
            v = baseline_val
        else:
            c = 'g'
            v = val
        plt.plot([v], [func(data[rows, :])], '*' + c)


if __name__ == '__main__':
    root = '/home/matte/Desktop/cs6787_fa2018/cs6787/logs'
    name = 'day_test_log_full_11-30_00-09-14_2.csv'
    # name, _, vals1 = show_best_daily_error(join(root, 'grid_search_512_2_layers_rep1'), 51, .02)
    # show_daily_error(join(root, 'grid_search_512_2_layers_rep1'), name)
    # plt.figure()
    # name, _, vals2 = show_best_daily_error(join(root, 'grid_search_512_2_layers_rep2'), 51, .02)
    # show_daily_error(join(root, 'grid_search_512_2_layers_rep2'), name)
    # plt.figure()
    # name, cw, vals3 = show_best_daily_error(join(root, 'grid_search_512_2_layers_rep3'), 51, .02)
    # show_daily_error(join(root, 'grid_search_512_2_layers_rep3'), name)
    # plt.figure()
    # plt.plot(cw, (vals1 + vals2 + vals3) / 3.)
    # plt.show()
    # plt.title('mean')
    #show_daily_error(join(root), name)

    name, _, vals2 = show_best_daily_error(join(root, '5_samples_repeats_.05', '1'), 0, .05)
    name, _, vals2 = show_best_daily_error(join(root, '5_samples_repeats_.05', '2'), 0, .05)
    plt.show()

    vals = []
    for i in range(1, 10):
        name, _, vals1 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '0.58_{}'.format(i)), .58, .02)
        vals.append(vals1)
    plt.figure()
    plt.plot(_, np.mean(vals, axis=0))
    # name, _, vals2 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '0.58_2'), .58, .02)
    # name, _, vals3 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '3'), 401, .02)
    # i = min(min(len(vals1), len(vals2)), len(vals3))
    # plt.figure()
    # plt.plot(_[:i], (vals1[:i] + vals2[:i] + vals3[:i]) / 3.)
    #
    # show_daily_error(join(root, 'gird_search_ae_repeats', '3'), name)
    plt.figure()

    show_resample(join(root, 'grid_search_resample'), 'Baseline', 'r')
    show_resample(join(root, 'grid_search_ae_resample_.645'), 'AE', 'g')
    plt.legend()
    plt.figure()

    compare_baseline(join(root, 'repeats_.645'), 0.645, func=np.max)
    compare_baseline(join(root, 'repeats_.05'), .05, func=np.max)
    compare_baseline(join(root, 'more_layers'), .05, baseline_val=-1, func=np.max)
    plt.show()
