# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.autograd import Variable

from tqdm import tqdm

from cs6787.model import MLP
from cs6787.load_data import NoaaDataset


def train(args):
    kwargs = {'num_workers': 2, 'pin_memory': True} if args.cuda else {}
    predicted_features = args.predicted_features.split(',')

    train_set = NoaaDataset(
        root=args.data, stage='train', predicted_features=predicted_features,
        include_invalid=args.include_invalid)
    train_loader = data.DataLoader(
        train_set, batch_size=args.batch_size, shuffle=True, **kwargs)

    test_stage = 'test' if args.test else 'val'
    test_set = NoaaDataset(
        root=args.data, stage=test_stage,
        predicted_features=predicted_features,
        include_invalid=args.include_invalid)
    test_loader = data.DataLoader(
        test_set, batch_size=args.batch_size, shuffle=True, **kwargs)

    net = MLP(train_set.x.shape[1], train_set.y.shape[1])
    print(net)

    if args.cuda:
        net.cuda()

    optimizer = optim.Adam(net.parameters(), lr=args.lr)
    decay = (0.000003 / args.lr) ** (1. / args.epochs)
    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, decay)
    criterion = nn.MSELoss()

    test_epoch(net, criterion, test_loader, args)
    for epoch in range(1, args.epochs+1):
        scheduler.step(epoch - 1)
        tr_loss, tr_acc = train_epoch(
            epoch, net, criterion, optimizer, train_loader, args)
        tt_loss, tt_acc = test_epoch(
            net, criterion, test_loader, args)


def train_epoch(epoch, net, criterion, optimizer, train_loader, args):
    losses = 0
    accs = 0
    net.train()

    for batch_idx, (data, target) in enumerate(tqdm(train_loader), 1):
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)

        optimizer.zero_grad()

        output = net(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        accs += (torch.mean((output - target) ** 2) ** .5).data.item()

        losses += loss.data.item()
    print("Epoch {0}: Train Loss={1:.3f}, Train Accuracy={2:.3f}".format(
        epoch, losses / batch_idx, accs / batch_idx))

    return losses / batch_idx, accs / batch_idx


def test_epoch(net, criterion, test_loader, args):
    net.eval()
    losses = 0
    accs = 0

    for batch_idx, (data, target) in enumerate(test_loader, 1):
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data), Variable(target)

        output = net(data)
        loss = criterion(output, target)

        accs += (torch.mean((output - target) ** 2) ** .5).data.item()

        losses += loss.data.item()
    print("\tTest Loss={0:.3f}, Test Accuracy={1:.3f}".format(
        losses / batch_idx, accs / batch_idx))
    return losses / batch_idx, accs / batch_idx
