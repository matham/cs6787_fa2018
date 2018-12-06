import numpy as np
from scipy.stats import ttest_ind, sem
from os.path import join
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import csv
from collections import defaultdict
import os
from functools import partial
import matplotlib as mpl

mpl.rc('figure', figsize=(3.375, 3.375*(.75)), titlesize=10)
mpl.rc('savefig', dpi=180)
mpl.rc('legend', scatterpoints=1, fontsize=10, frameon=False)
mpl.rc('font', size=10, family='serif', weight='normal', serif=['Computer Modern Roman'])
mpl.rc('axes', labelsize=10, titlesize=10, labelweight='normal')
mpl.rc('xtick', labelsize=10)
mpl.rc('ytick', labelsize=10)


def cohend(d1, d2):
    # calculate the size of samples
    n1, n2 = len(d1), len(d2)
    # calculate the variance of the samples
    s1, s2 = np.var(d1, ddof=1), np.var(d2, ddof=1)
    # calculate the pooled standard deviation
    s = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    # calculate the means of the samples
    u1, u2 = np.mean(d1), np.mean(d2)
    # calculate the effect size
    return (u1 - u2) / s


def get_data(root, name, clear_unseen=True):
    with open(join(root, name)) as fh:
        reader = csv.reader(fh)
        lines = list(reader)[2:]

        n = (len(lines[0]) - 1) / 3
        assert n.is_integer()
        n = int(n)

        data = np.array([list(map(float, line[n + 1: 2 * n + 1])) for line in lines])
        days = np.array([int(line[0]) for line in lines])
        if clear_unseen:
            for row in range(data.shape[0]):
                data[row, row + 1:] = 0
        return days, data


def show_daily_error(root, name, clear_unseen=True):
    days, data = get_data(root, name, clear_unseen)
    test_days = np.arange(data.shape[1])
    days = days[:, np.newaxis].repeat(len(test_days), 1)
    test_days = test_days[np.newaxis, :].repeat(data.shape[0], 0)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(
        days[:, :], test_days[:, :], data[:, :], cmap=cm.coolwarm, linewidth=0,
        antialiased=False)
    plt.xlabel('Train Interval')
    plt.ylabel('Test Interval')
    ax.set_zlim(0, .15)


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
    #print('min max-error is "{}" for file "{}" at time "{}"'.format(vals[i], files[i], cw[i]))
    sort_i = np.argsort(vals)
    #print(vals[sort_i])
    #print([files[i] for i in sort_i])
    #print(cw[sort_i])
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


def compare_baseline(root, val, baseline_val=0., func=np.max, rows=slice(None), plot=True):
    files = [f for f in os.listdir(root) if f.startswith('day_test_log_full_')]

    values = {val: [], baseline_val: []}
    for filename in files:
        try:
            data = get_data(root, filename)[1]
        except Exception as e:
            print('Skipping {}, {}'.format(filename, e))
            continue
        if np.isnan(data).any() or data.shape[0] != 35:
            print('skipping {}'.format(filename))
            continue

        if 'False' in filename:
            c = 'r'
            v = baseline_val
        else:
            c = 'g'
            v = val

        res = func(data[rows, :])
        values[v].append(res)
        if plot:
            plt.plot([v], [res], '*' + c, label=None)
    return values


if __name__ == '__main__':
    root = '/home/matte/Desktop/cs6787_fa2018/cs6787/logs'
    name = 'day_test_log_full_12-04_23-40-15.csv'
    # y = get_data(join(root, 'test_result'), name)[1][-1, :]
    # plt.plot(y)
    # plt.show()
    # exit()

    # name, _, vals1 = show_best_daily_error(join(root, 'grid_search_cw_normalize'), 0, .02)
    # plt.xlabel('WCL $\lambda$')
    # plt.ylabel('MSE')
    # show_daily_error(join(root, 'grid_search_512_2_layers_rep1'), name)
    # plt.show()
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

    # name, _, vals2 = show_best_daily_error(join(root, '5_samples_repeats_.05', '1'), 0, .1)
    # name, _, vals2 = show_best_daily_error(join(root, '5_samples_repeats_.05', '2'), 0, .1)
    # plt.show()

    # vals = []
    # for i in range(1, 4):
    #     name, _, vals1 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '{}'.format(i)), 0, .02)
    #     vals.append(vals1)
    # n = np.min([len(item) for item in vals])
    # vals = [item[:n] for item in vals]
    # mean = np.mean(vals, axis=0)
    # plt.plot(_[:n], mean, linewidth=5.0)
    # plt.plot([.641236], [.105348], 'k*', markersize=10.0)
    # plt.xlabel('AE $\lambda$')
    # plt.ylabel('MSE')
    # plt.xlim(0, .68)

    # name, _, vals2 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '0.58_2'), .58, .02)
    # name, _, vals3 = show_best_daily_error(join(root, 'gird_search_ae_repeats', '3'), 401, .02)
    # i = min(min(len(vals1), len(vals2)), len(vals3))
    # plt.figure()
    # plt.plot(_[:i], (vals1[:i] + vals2[:i] + vals3[:i]) / 3.)
    #
    # show_daily_error(join(root, 'gird_search_ae_repeats', '3'), name)
    # plt.figure()

    # show_resample(join(root, 'grid_search_resample'), 'Baseline', 'r')
    # show_resample(join(root, 'grid_search_ae_resample_.645'), 'AE', 'g')
    # plt.xlabel('Re-sampling count')
    # plt.ylabel('Prediction MSE')
    # plt.legend()
    # plt.figure()

    # res = compare_baseline(join(root, 'repeats_.645'), 0.645, func=np.max)
    # print(np.mean(res[0]), np.mean(res[0.645]), ttest_ind(res[0], res[0.645], equal_var=False))
    # res = compare_baseline(join(root, 'repeats_.05'), .05, func=np.max)
    # print(np.mean(res[0]), np.mean(res[0.05]), ttest_ind(res[0], res[0.05], equal_var=False))
    # compare_baseline(join(root, 'more_layers'), .05, baseline_val=-1, func=np.max)

    # plt.figure()
    # first = True
    # for resample, base, ae in (('0', 0, 1), ('5', 4, 5), ('100', 8, 9)):
    #     res = compare_baseline(join(root, 'test_result', resample), ae, base, func=np.max, plot=False)
    #     p = ttest_ind(res[base], res[ae], equal_var=False).pvalue
    #     n = min(len(res[base]), len(res[ae]))
    #     base_mean = np.mean(res[base])
    #     ae_mean = np.mean(res[ae])
    #     d = cohend(res[base], res[ae])
    #
    #     plt.bar([base], [base_mean], 1, alpha=.4, label='Baseline' if first else None, color='b')
    #     plt.bar([ae], [ae_mean], 1, alpha=.4, label='AE' if first else None, color='r')
    #     plt.errorbar(base, base_mean, yerr=sem(res[base]), capsize=5, ecolor='k')
    #     plt.errorbar(ae, ae_mean, yerr=sem(res[ae]), capsize=5, ecolor='k')
    #
    #     y, h = .215, .01
    #     if p <= .0001:
    #         s = '****'
    #     elif p <= 0.001:
    #         s = '***'
    #     elif p <= 0.01:
    #         s = '**'
    #     elif p <= 0.05:
    #         s = '*'
    #     else:
    #         s = 'ns'
    #     plt.plot([base, base, ae, ae], [y, y + h, y + h, y], lw=1.5, c='k')
    #     plt.text((base + ae) / 2., y + h, s, ha='center', va='bottom', color='k')
    #
    #     first = False
    #
    #     if p < .01:
    #         f = 'e'
    #     else:
    #         f = 'f'
    #
    #     print(('{} & {:0.2f} & {:0.2f} & {:0.2f} & {:0.2' + f + '} & {} \\\\\n\\hline').format(
    #         resample, base_mean, ae_mean, d, p, n))
    #
    # ae, base = -500, -1
    # res = compare_baseline(join(root, 'test_result', '4_layers'), ae, base, func=np.max, plot=False)
    # n = len(res[base])
    # base_mean = np.mean(res[base])
    #
    # plt.bar([base], [base_mean], 1, alpha=.4, label='Baseline-4', color='g')
    # plt.errorbar(base, base_mean, yerr=sem(res[base]), capsize=5, ecolor='k')
    #
    # plt.xticks([0, 4.5, 8.5], ['0', '5', '100'])
    # plt.xlabel('Re-sampling count')
    # plt.ylabel('Prediction MSE')
    # plt.legend()

    # plt.figure()
    # train = np.loadtxt('/home/matte/Desktop/train.csv', delimiter=',')
    # test = np.loadtxt('/home/matte/Desktop/test.csv', delimiter=',')
    # plt.plot(train[:, 0], train[:, 1], '--r', label='Baseline Train')
    # plt.plot(train[:, 0], train[:, 2], '--g', label='AE Train')
    # plt.plot(test[1:, 0], test[1:, 1], ':r', label='Baseline Test')
    # plt.plot(test[1:, 0], test[1:, 2], ':g', label='AE Test')
    # plt.xlabel('Training Interval')
    # plt.ylabel('Prediction MSE')
    # plt.legend()

    show_daily_error(join(root, 'test_result'), 'day_test_log_full_12-05_20-14-17.csv', False)
    plt.show()
    days, data = get_data(join(root, 'test_result'), 'day_test_log_full_12-05_20-14-17.csv', False)
    plt.plot(data[-1, :])
    plt.xlabel('Test Interval')
    plt.ylabel('MSE')
    plt.show()
