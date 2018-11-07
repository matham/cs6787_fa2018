# -*- coding: utf-8 -*-

import argparse
from cs6787.train import train


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Online learning')
    parser.add_argument('--cuda', type=bool, default=False,
            help='Use cuda or not')
    parser.add_argument('--in_features', type=int, default=784,
            help='input features dim')
    parser.add_argument('--out_features', type=int, default=10,
            help='output features dim')
    parser.add_argument('--batch_size', type=int, default=200,
            help='batch size')
    parser.add_argument('--test_batch_size', type=int, default=1000,
            help='batch size')
    parser.add_argument('--lr', type=float, default=0.001,
            help='Learning rate')
    parser.add_argument('--epochs', type=int, default=26,
            help='Epochs')
    args = parser.parse_args()

    train(args)
