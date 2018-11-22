import torch
from torch.optim.optimizer import Optimizer, required


class SGDCW(Optimizer):

    def __init__(self, params, lr=required, momentum=0, cw_weight=0):
        if lr is not required and lr < 0.0:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if momentum < 0.0:
            raise ValueError("Invalid momentum value: {}".format(momentum))
        if cw_weight < 0.0:
            raise ValueError("Invalid cw_weight value: {}".format(cw_weight))

        defaults = dict(lr=lr, momentum=momentum, cw_weight=cw_weight)
        super(SGDCW, self).__init__(params, defaults)

    def __setstate__(self, state):
        super(SGDCW, self).__setstate__(state)
        for group in self.param_groups:
            group.setdefault('nesterov', False)

    def step(self, closure=None):
        """Performs a single optimization step.

        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            cw_weight = group['cw_weight']
            momentum = group['momentum']

            for p in group['params']:
                if p.grad is None:
                    continue
                d_p = p.grad.data

                state = self.state[p]

                if cw_weight != 0:
                    if 'cw_grad' not in state:
                        state['cw_grad'] = torch.zeros_like(p.data)
                        state['cw_grad2'] = torch.zeros_like(p.data)
                        state['cw_grad2'].copy_(d_p)
                    else:
                        state['cw_grad'].copy_(d_p)
                        d_p.add_(cw_weight, state['cw_grad2'])
                        state['cw_grad2'].copy_(state['cw_grad'])

                if momentum != 0:
                    param_state = self.state[p]
                    if 'momentum_buffer' not in param_state:
                        buf = param_state['momentum_buffer'] = torch.zeros_like(p.data)
                        buf.mul_(momentum).add_(d_p)
                    else:
                        buf = param_state['momentum_buffer']
                        buf.mul_(momentum).add_(1, d_p)
                    d_p = buf

                p.data.add_(-group['lr'], d_p)

        return loss
