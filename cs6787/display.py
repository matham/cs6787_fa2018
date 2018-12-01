import numpy as np
from os.path import join
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import csv
import os

matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams['savefig.dpi'] = 300


def show_daily_error(root, name):
    with open(join(root, name)) as fh:
        reader = csv.reader(fh)
        lines = list(reader)

        header = lines.pop(0)
        lines.pop(0)

        n = (len(header) - 1) / 3
        assert n.is_integer()
        n = int(n)

        data = np.array([list(map(float, line[n + 1: 2 * n + 1])) for line in lines])
        days = np.array([int(line[0]) for line in lines])
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

        plt.show()


def show_best_daily_error(root, count=201, mult=.01):
    files_ = [f for f in os.listdir(root) if f.startswith('day_test_log_full_')]
    times = [os.path.getmtime(join(root, f)) for f in files_]
    files_ = sorted(files_, key=lambda f: times[files_.index(f)])

    vals = []
    files = []
    cw = []
    i = 0
    for filename in files_:
        with open(join(root, filename)) as fh:
            reader = csv.reader(fh)
            lines = list(reader)[2:]

            n = (len(lines[0]) - 1) / 3
            assert n.is_integer()
            n = int(n)

            data = np.array([list(map(float, line[n + 1: 2 * n + 1])) for line in lines])[5:, :]
            if np.isnan(data).any():
                i += 1
                continue

            max_val = data.max()
            vals.append(max_val)
            cw.append(i * mult)
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
    plt.tight_layout()
    plt.draw()
    plt.show()
    return files[i], cw, vals


if __name__ == '__main__':
    root = '/home/matte/Desktop/cs6787_fa2018/cs6787/logs'
    name = 'day_test_log_full_11-30_00-43-10_2.csv'
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

    name, _, vals1 = show_best_daily_error(join(root, 'grid_search_ae'), 101, .02)
    show_daily_error(join(root, 'grid_search_ae'), name)
