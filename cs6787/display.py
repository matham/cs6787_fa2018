import numpy as np
from os.path import join
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import csv

matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams['savefig.dpi'] = 300

root = '/home/matte/Desktop/cs6787_fa2018/cs6787/logs'
name = 'day_test_log_full_11-23_16-26-49.csv'

with open(join(root, name)) as fh:
    reader = csv.reader(fh)
    lines = list(reader)

    header = lines.pop(0)
    lines.pop(0)

    n = (len(header) - 1) / 3
    assert n.is_integer()
    n = int(n)

    data = np.array([list(map(float, line[1: n + 1])) for line in lines])
    days = np.array([int(line[0]) for line in lines])
    test_days = np.arange(data.shape[1])
    days = days[:, np.newaxis].repeat(len(test_days), 1)
    test_days = test_days[np.newaxis, :].repeat(data.shape[0], 0)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(
        days, test_days, data, cmap=cm.coolwarm, linewidth=0,
        antialiased=False)
    plt.xlabel('Day')
    plt.ylabel('Test days')
    plt.title('SGD Randomized')

    plt.show()
