# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable


class MLP(nn.Module):
    def __init__(self, in_features, out_features, num_units=2048):
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
                nn.BatchNorm1d(out_features, eps=1e-4, momentum=0.15),
                nn.LogSoftmax()
                )

    def forward(self, x):
        return self.net(x)
