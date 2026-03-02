import torch
import torch.optim as optim
from model import EconomicModel

def train():
    model = EconomicModel()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(100):
        x = torch.randn(64, 2)
        y = torch.sum(x, dim=1, keepdim=True)

        pred = model(x)
        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), "economic_model.pt")

if __name__ == "__main__":
    train()
