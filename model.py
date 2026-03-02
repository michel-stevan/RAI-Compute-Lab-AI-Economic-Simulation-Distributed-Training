import torch
import torch.nn as nn

class EconomicModel(nn.Module):
    def __init__(self):
        super(EconomicModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.net(x)
