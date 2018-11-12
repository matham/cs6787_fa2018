# -*- coding: utf-8 -*-

import argparse
from cs6787.train import train


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Online learning')
    parser.add_argument(
        '--cuda', dest='cuda', action='store_const', const=True, default=False,
        help='Use cuda or not')
    parser.add_argument(
        '--test', dest='test', action='store_const', const=True, default=False,
        help='Use test dataset')
    parser.add_argument(
        '--include_invalid', dest='include_invalid', action='store_const',
        const=True, default=False, help='If to include rows with invalid data')
    parser.add_argument(
        '--predicted_features', type=str,
        default="temp-10pctl,temp-90pctl,temp-normal",
        help='features to predict')
    parser.add_argument(
        '--batch_size', type=int, default=200, help='batch size')
    parser.add_argument(
        '--data', type=str, default='', help='data path')
    parser.add_argument(
        '--lr', type=float, default=0.001, help='Learning rate')
    parser.add_argument(
        '--epochs', type=int, default=26, help='Epochs')
    args = parser.parse_args()

    train(args)
