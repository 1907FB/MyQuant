import torch
import torch.nn as nn


class TorchSquare(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def forward(self, x):
        return x * x
