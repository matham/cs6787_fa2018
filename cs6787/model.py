# -*- coding: utf-8 -*-
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, in_features, out_features, num_units=512):
        super(MLP, self).__init__()

        self.net = nn.Sequential(
                nn.Linear(in_features, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU(),
                nn.Linear(num_units, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU(),
                nn.Linear(num_units, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU(),
                nn.Linear(num_units, out_features),
        )

    def forward(self, x):
        return self.net(x)
