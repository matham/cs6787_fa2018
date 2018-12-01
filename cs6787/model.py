# -*- coding: utf-8 -*-
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, in_features, out_features, num_units=512, n_layers=2):
        super(MLP, self).__init__()

        self.net = nn.Sequential(
                nn.Linear(in_features, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU())
        for i in range(n_layers):
            self.net.add_module('online_0_{}'.format(i), nn.Linear(num_units, num_units))
            self.net.add_module('online_1_{}'.format(i), nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15))
            self.net.add_module('online_2_{}'.format(i), nn.ReLU())
        self.net.add_module('online_final', nn.Linear(num_units, out_features))

    def forward(self, x):
        return self.net(x)
