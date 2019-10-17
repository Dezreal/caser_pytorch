import torch
from torch import nn
from time import time
import numpy as np

size = 5000
n = 100000

x = torch.zeros(5, 5, size)
v = torch.ones(size)


index1 = torch.ones(size, dtype=torch.long)
index3 = torch.arange(0, size)
indices = [index1, index1, index3]

t1 = time()
for i in range(n):
    x[1, 1, 0:size] = v
t2 = time()

t3 = time()
for j in range(n):
    x.index_put_(indices, v)
t4 = time()

print(t2 - t1)
print(t4 - t3)

print((t4 - t3) / (t2 - t1))
