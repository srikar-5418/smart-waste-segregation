import torch
import torchvision.models as models
from torch.nn import Linear


def get_model():
    model = models.resnet34(pretrained=True)
    model.fc = Linear(in_features=512, out_features=6)
    return model
