# -*- coding: utf-8 -*-
import torch.nn as nn
import torch
from torch.autograd import Variable
import torch.nn.functional as F


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


class MLPVAE(nn.Module):

    def __init__(self, in_features, out_features, num_units=512, n_layers=2):
        super(MLPVAE, self).__init__()

        self.encoder = nn.Sequential(
                nn.Linear(in_features, num_units),
                nn.BatchNorm1d(num_units, eps=1e-4, momentum=0.15),
                nn.ReLU())
        self.encoder.add_module('online_0', nn.Linear(num_units, 400))
        self.encoder.add_module('online_1', nn.BatchNorm1d(400, eps=1e-4, momentum=0.15))
        self.encoder.add_module('online_2', nn.ReLU())
        self.encoder.add_module('online_3', nn.Linear(400, 200))
        self.encoder.add_module('online_4', nn.BatchNorm1d(200, eps=1e-4, momentum=0.15))
        self.encoder.add_module('online_5', nn.ReLU())
        self.proj_mean = nn.Linear(200, 100)
        self.proj_var = nn.Linear(200, 100)

        self.pred = nn.Linear(200, out_features)

        self.decoder = nn.Sequential()
        self.decoder.add_module('online_0', nn.Linear(100, 200))
        self.decoder.add_module('online_1', nn.BatchNorm1d(200, eps=1e-4, momentum=0.15))
        self.decoder.add_module('online_2', nn.ReLU())
        self.decoder.add_module('online_3', nn.Linear(200, 400))
        self.decoder.add_module('online_4', nn.BatchNorm1d(400, eps=1e-4, momentum=0.15))
        self.decoder.add_module('online_5', nn.ReLU())

        self.recons = nn.Linear(400, in_features)

    def reparametrize(self, mu, logvar):
        std = logvar.mul(0.5).exp_()
        if torch.cuda.is_available():
            eps = torch.cuda.FloatTensor(std.size()).normal_()
        else:
            eps = torch.FloatTensor(std.size()).normal_()
        eps = Variable(eps)
        return eps.mul(std).add_(mu)

    def forward(self, x):
        h = self.encoder(x)
        predicted = self.pred(h)
        mu = self.proj_mean(h)
        logvar = self.proj_var(h)
        z = self.reparametrize(mu, logvar)
        return predicted, F.sigmoid(self.recons(self.decoder(z))), mu, logvar

    def loss_function(self, mse_loss, recon_x, x, mu, logvar):
        BCE = mse_loss(recon_x, x)  # mse loss
        # loss = 0.5 * sum(1 + log(sigma^2) - mu^2 - sigma^2)
        KLD_element = mu.pow(2).add_(logvar.exp()).mul_(-1).add_(1).add_(logvar)
        KLD = torch.sum(KLD_element).mul_(-0.5)
        # KL divergence
        return BCE + KLD
