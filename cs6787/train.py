# -*- coding: utf-8 -*-
from os.path import join, dirname
import time
import sys

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.autograd import Variable

from tqdm import tqdm

from cs6787.model import MLP
from cs6787.optimizer import SGDCW
from cs6787.load_data import NoaaDataset


def train(args):
    kwargs = {'num_workers': 2, 'pin_memory': True} if args.cuda else {}
    predicted_features = args.predicted_features.split(',')

    train_set = NoaaDataset(
        root=args.data, stage='train', predicted_features=predicted_features,
        include_invalid=args.include_invalid, epoch_days=args.epoch_days,
        warm_epoch_days=args.warm_epoch_days,
        randomize_samples=args.randomize_samples, rotate_data=args.rotate_data)
    train_loader = data.DataLoader(
        train_set, batch_size=args.batch_size, shuffle=True, **kwargs)
    print('loaded train data')

    test_stage = 'test' if args.test else 'val'
    test_set = NoaaDataset(
        root=args.data, stage=test_stage,
        predicted_features=predicted_features,
        include_invalid=args.include_invalid, epoch_days=args.epoch_days,
        warm_epoch_days=args.warm_epoch_days,
        randomize_samples=args.randomize_samples)
    test_loader = data.DataLoader(
        test_set, batch_size=args.batch_size, shuffle=True, **kwargs)
    print('loaded test data')

    net = MLP(train_set.x.shape[1] - 1, train_set.y.shape[1])
    print(net)

    if args.cuda:
        net.cuda()

    if not args.epoch_days:
        fname = time.strftime('log_%m-%d_%H-%M-%S.csv')
        with open(join(dirname(__file__), 'logs', 'README.md'), 'a') as fh:
            fh.write(fname)
            fh.write('\n')
            fh.write(repr(args))
            fh.write('\n')
            fh.write(' '.join(sys.argv))
            fh.write('\n\n')

        with open(join(dirname(__file__), 'logs', fname), 'w') as log_fh:
            train_offline(args, net, train_loader, test_loader, log_fh)
    else:
        daily_fname = time.strftime('day_test_log_full_%m-%d_%H-%M-%S.csv')
        fname = time.strftime('day_log_%m-%d_%H-%M-%S.csv')
        with open(join(dirname(__file__), 'logs', 'README.md'), 'a') as fh:
            fh.write('{}, {}\n'.format(daily_fname, fname))
            fh.write(repr(args))
            fh.write('\n')
            fh.write(' '.join(sys.argv))
            fh.write('\n\n')

        with open(join(
                dirname(__file__), 'logs', daily_fname), 'w') as day_log_fh:
            with open(join(dirname(__file__), 'logs', fname), 'w') as log_fh:
                train_online(
                    args, net, train_loader, test_loader, day_log_fh, log_fh)


def train_offline(args, net, train_loader, test_loader, log_fh):
    optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9)
    decay = (0.000003 / args.lr) ** (1. / args.epochs)
    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, decay)
    criterion = nn.MSELoss()

    n, tt_loss, tt_acc = test_epoch(net, criterion, test_loader, args)
    print("Test Loss={0:.3f}, Test MSE={1:.3f}, N={2}".format(
        tt_loss, tt_acc, n))

    log_fh.write(
        'Epoch,Train Loss,Train MSE,Train N,Test Loss,Test MSE,Test N\n')
    log_fh.write('-1,0,0,0,{},{},{}\n'.format(tt_loss, tt_acc, n))

    for epoch in range(1, args.epochs + 1):
        scheduler.step(epoch - 1)
        n, tr_loss, tr_acc = train_epoch(
            net, criterion, optimizer, train_loader, args)
        print("Epoch {0}:\tTrain Loss={1:.3f},\tTrain MSE={2:.3f},\tN={3}".
              format(epoch, tr_loss, tr_acc, n), end='')

        n_test, tt_loss, tt_acc = test_epoch(
            net, criterion, test_loader, args)
        print(",\tTest Loss={0:.3f},\tTest MSE={1:.3f},\tN={2}".format(
            tt_loss, tt_acc, n_test))

        log_fh.write(
            '{},{},{},{},{},{},{}\n'.format(
                epoch, tr_loss, tr_acc, n, tt_loss, tt_acc, n_test))
        log_fh.flush()


def train_online(args, net, train_loader, test_loader, day_log_fh, log_fh):
    optimizer = SGDCW(net.parameters(), lr=args.lr, momentum=0.9)
    decay = (0.000003 / args.lr) ** (1. / args.epochs)
    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, decay)
    criterion = nn.MSELoss()

    res = [], [], []
    tqdm_it = tqdm(
        leave=False, unit='Samples', total=test_loader.dataset.total_size)

    for day in range(len(test_loader.dataset.days)):
        test_loader.dataset.day = day
        n, tt_loss, tt_acc = test_epoch(
            net, criterion, test_loader, args, tqdm_it)

        res[2].append(n)
        res[0].append(tt_loss)
        res[1].append(tt_acc)

    tqdm_it.close()
    day_log_fh.write('Day,{}{}{}\n'.format(
        'Train Loss,' * len(res[1]), 'Train MSE,' * len(res[1]),
        ('N,' * len(res[1]))[:-1]))
    day_log_fh.write('0,{}\n'.format(
        ','.join(
            (','.join(map(str, v)) for v in res)
        )
    ))
    day_log_fh.flush()

    test_loader.dataset.day = 0
    n, tt_loss, tt_acc = test_epoch(net, criterion, test_loader, args)
    print("Day 0\tTest Loss={0:.3f},Test MSE={1:.3f}, N={2}".format(
        tt_loss, tt_acc, n))

    log_fh.write(
        'Day,Epoch,Train Loss,Train MSE,Train N,Test Loss,Test MSE,Test N\n')
    log_fh.write('0,-1,0,0,0,{},{},{}\n'.format(tt_loss, tt_acc, n))
    log_fh.flush()

    for day in range(len(train_loader.dataset.days)):
        train_loader.dataset.day = day
        test_loader.dataset.day = day
        n_epochs = args.epochs_warm if not day else args.epochs

        if day == 1:
            if args.cw_weight:
                for group in optimizer.param_groups:
                    group['cw_weight'] = args.cw_weight

        for epoch in range(1, n_epochs + 1):
            scheduler.step(epoch - 1)
            n, tr_loss, tr_acc = train_epoch(
                net, criterion, optimizer, train_loader, args)
            n_test, tt_loss, tt_acc = test_epoch(
                net, criterion, test_loader, args)

            print("Day {4}\tEpoch {0}:\tTrain Loss={1:.3f},\t"
                  "Train MSE={2:.3f},\tN={3}"
                  .format(epoch, tr_loss, tr_acc, n, day), end='')
            print(",\tTest Loss={0:.3f},\tTest MSE={1:.3f},\tN={2}".
                  format(tt_loss, tt_acc, n_test))

            log_fh.write(
                '{},{},{},{},{},{},{},{}\n'.format(
                    day, epoch, tr_loss, tr_acc, n, tt_loss, tt_acc, n_test))
            log_fh.flush()

        res = [], [], []
        tqdm_it = tqdm(
            leave=False, unit='Samples', total=test_loader.dataset.total_size)
        for day_ in range(len(test_loader.dataset.days)):
            test_loader.dataset.day = day_
            n, tt_loss, tt_acc = test_epoch(
                net, criterion, test_loader, args, tqdm_it)

            res[2].append(n)
            res[0].append(tt_loss)
            res[1].append(tt_acc)

        tqdm_it.close()
        day_log_fh.write('{},{}\n'.format(
            day, ','.join(
                (','.join(map(str, v)) for v in res)
            )
        ))
        day_log_fh.flush()


def train_epoch(net, criterion, optimizer, train_loader, args):
    losses = 0
    mse = 0
    n = 0
    batch_idx = 1
    net.train()
    tqdm_it = tqdm(
        leave=False, unit='Samples', total=len(train_loader.dataset))

    for batch_idx, (data, target) in enumerate(train_loader, 1):
        if target.shape[0] <= 1:
            continue

        n += target.shape[0]
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)

        optimizer.zero_grad()

        output = net(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        mse += torch.mean((output - target) ** 2).data.item()
        losses += loss.data.item()

        tqdm_it.update(target.shape[0])

    tqdm_it.close()
    return n, losses / batch_idx, mse / batch_idx


def test_epoch(net, criterion, test_loader, args, tqdm_obj=None):
    net.eval()
    losses = 0
    mse = 0
    n = 0
    batch_idx = 1

    tqdm_it = tqdm_obj
    if tqdm_it is None:
        tqdm_it = tqdm(
            leave=False, unit='Samples', total=len(test_loader.dataset))

    for batch_idx, (data, target) in enumerate(test_loader, 1):
        if target.shape[0] <= 1:
            continue

        n += target.shape[0]
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)

        output = net(data)
        loss = criterion(output, target)

        mse += torch.mean((output - target) ** 2).data.item()
        losses += loss.data.item()

        tqdm_it.update(target.shape[0])

    if tqdm_obj is None:
        tqdm_it.close()
    return n, losses / batch_idx, mse / batch_idx
