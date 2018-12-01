import torch
from torch.optim.optimizer import Optimizer, required


class SGDCW(Optimizer):

    def __init__(self, params, lr=required, momentum=0, cw_weight=0,
                 beta=0.999, eps=1e-8, use_kl_div=False,
                 use_last_loss=False):
        if lr is not required and lr < 0.0:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if momentum < 0.0:
            raise ValueError("Invalid momentum value: {}".format(momentum))
        if cw_weight < 0.0:
            raise ValueError("Invalid cw_weight value: {}".format(cw_weight))
        if not 0.0 <= beta < 1.0:
            raise ValueError("Invalid beta parameter at index 1: {}".format(beta))
        if not 0.0 <= eps:
            raise ValueError("Invalid epsilon value: {}".format(eps))

        defaults = dict(lr=lr, momentum=momentum, cw_weight=cw_weight,
                        beta=beta, eps=eps, use_kl_div=use_kl_div,
                        use_last_loss=use_last_loss)
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
            use_kl_div = group['use_kl_div']
            use_last_loss = group['use_last_loss']

            for p in group['params']:
                if p.grad is None:
                    continue
                d_p = p.grad.data

                state = self.state[p]

                if 'last_cw_grad' not in state:
                    state['last_cw_grad'] = torch.zeros_like(p.data)
                if 'grad_sum' not in state:
                    state['grad_sum'] = torch.zeros_like(p.data)

                # State initialization
                if use_kl_div:
                    if 'step' not in state:
                        state['step'] = 0
                        state['exp_avg_sq'] = torch.zeros_like(p.data)
                    state['step'] += 1

                    if cw_weight != 0:
                        d_p.addcdiv_(
                            cw_weight, state['last_cw_grad'],
                            state['exp_avg_sq'] / (1 - group['beta'] ** state['step']) + group['eps'])
                        if torch.isnan(d_p).any() and False:
                            print('dp', d_p)
                            print('grad', state['last_cw_grad'])
                            print('sq', state['exp_avg_sq'])
                            print((1 - group['beta'] ** state['step']), group['eps'])
                            print(state['exp_avg_sq'] / (1 - group['beta'] ** state['step']) + group['eps'])
                            print('isnane', torch.isnan(
                                state['exp_avg_sq'] / (1 - group['beta'] ** state['step']) + group['eps']).any(),
                                  torch.isnan(d_p).any())
                            exit()

                elif cw_weight:
                    if use_last_loss:
                        d_p.add_(cw_weight, state['last_cw_grad'])
                    else:
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

                state['last_cw_grad'].copy_(-group['lr'] * d_p)
                if use_kl_div:
                    state['exp_avg_sq'].mul_(group['beta']).addcmul_(1 - group['beta'], p.data, p.data)
                state['grad_sum'].add_(-group['lr'], d_p)
                p.data.add_(-group['lr'], d_p)

        return loss
