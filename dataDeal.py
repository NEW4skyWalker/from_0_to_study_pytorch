import torch

x=torch.arange(12,dtype=torch.float32).reshape(3,4)
y=torch.tensor([[2.0,2,2,2],[2,1,2,1],[1,2,3,1]])
print(torch.cat((x,y),dim=0))
print(torch.cat((x,y),dim=1))
print(x.sum())
