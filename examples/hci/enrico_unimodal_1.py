import sys
import os
from torch import nn
sys.path.append(os.getcwd())
from training_structures.unimodal import train, test
from fusions.common_fusions import Concat
from datasets.enrico.get_data import get_dataloader
from unimodals.common_models import VGG16, VGG16Slim,DAN,Linear,MLP, VGG11Slim, VGG11Pruned

import torch

dls, weights = get_dataloader('datasets/enrico/dataset')
traindata, validdata, testdata = dls
modalnum = 1
encoder=VGG11Slim(16, dropout=True, dropoutp=0.2, freeze_features=True).cuda()
head = Linear(16, 20).cuda()
# head = MLP(16, 16, 20, dropout=False).cuda()

train(encoder,head,traindata,validdata,50,optimtype=torch.optim.Adam,lr=0.0001,weight_decay=0,modalnum=modalnum)

print("Testing:")
model=torch.load('best.pt').cuda()
test(encoder,head , testdata, modalnum=modalnum)

