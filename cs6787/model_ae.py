# -*- coding: utf-8 -*-
import torch.nn as nn


class MLPAE(nn.Module):

    def __init__(self, in_features, out_features, num_units=512, n_layers=2):
        super(MLPAE, self).__init__()

        self.encoder = nn.Sequential(
                nn.Linear(in_features, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU())
        for i in range(n_layers):
            self.encoder.add_module('online_0_{}'.format(i), nn.Linear(num_units, num_units))
            self.encoder.add_module('online_1_{}'.format(i), nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15))
            self.encoder.add_module('online_2_{}'.format(i), nn.ReLU())

        self.pred = nn.Linear(num_units, out_features)

        self.decoder = nn.Sequential()
        for i in range(n_layers):
            self.decoder.add_module('online2_0_{}'.format(i), nn.Linear(num_units, num_units))
            self.decoder.add_module('online2_1_{}'.format(i), nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15))
            self.decoder.add_module('online2_2_{}'.format(i), nn.ReLU())

        self.recons = nn.Linear(num_units, in_features)

    def forward(self, x):
        h = self.encoder(x)
        predicted = self.pred(h)
        return predicted, self.recons(self.decoder(h))
