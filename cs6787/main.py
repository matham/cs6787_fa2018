# -*- coding: utf-8 -*-

import argparse
from cs6787.train import train


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Online learning')
    parser.add_argument(
        '--cuda', dest='cuda', action='store_const', const=True, default=False,
        help='Whether to use cuda')
    parser.add_argument(
        '--test', dest='test', action='store_const', const=True, default=False,
        help='Whether to use the test or val dataset')
    parser.add_argument(
        '--include_invalid', dest='include_invalid', action='store_const',
        const=True, default=False, help='If to include rows with invalid data')
    parser.add_argument(
        '--predicted_features', type=str,
        default="temp-10pctl,temp-90pctl,temp-normal",
        help='Features to predict')
    parser.add_argument(
        '--batch_size', type=int, default=200, help='The batch size')
    parser.add_argument(
        '--data', type=str, default='', help='The data path')
    parser.add_argument(
        '--lr', type=float, default=0.001, help='Learning rate')
    parser.add_argument(
        '--epochs', type=int, default=26, help='Number of epochs')
    parser.add_argument(
        '--epochs_warm', type=int, default=5, help='Number of epochs')
    parser.add_argument(
        '--epoch_days', type=float, default=0,
        help='Number of days in an epoch when trained online')
    parser.add_argument(
        '--warm_epoch_days', type=float, default=30 * 6,
        help='Number of days in an epoch when trained online for the warmup')
    parser.add_argument(
        '--randomize_samples', dest='randomize_samples', action='store_const',
        const=True, default=False,
        help='Whether to randomize the time of the examples')
    parser.add_argument(
        '--rotate_data', dest='rotate_data', action='store_const', const=True,
        default=False, help='Whether to shift the train data halfway')
    args = parser.parse_args()

    train(args)
