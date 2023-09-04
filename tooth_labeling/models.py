import torch
import torch.nn as nn
from torchvision.models import resnet34, ResNet34_Weights

resnet34 = resnet34(weights=ResNet34_Weights.DEFAULT)

num_classes = 5  
resnet34.fc = nn.Linear(resnet34.fc.in_features, num_classes)

for param in resnet34.parameters():
    param.requires_grad = True