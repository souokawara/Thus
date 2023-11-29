import FOURIER as fourier
import torch
# import torchquad

# base frequency
# Hz
f0 = torch.tensor(440000)

# exponential indices
n = torch.arange(-20,20,1)
a = 2**(n.float())

# frequencies
fs = a*f0

print(fs)
