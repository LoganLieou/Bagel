import torch
from torch import nn
from torch.utils.data import DataLoader
from torchtext import datasets

train_data = datasets.IMDB(
   root=".data",
   split="train"
)

test_data = datasets.IMDB(
   root=".data",
   split="test"
)

batch_size = 64

train_dataloader = DataLoader(train_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

class Network(nn.Module):
   def __init__(self, in_size: int = 28, out_size = 2):
      super(Network, self).__init__()
      pass
   def forward(self, x: torch.Tensor) -> torch.Tensor:
      pass

model = Network()

print(model)