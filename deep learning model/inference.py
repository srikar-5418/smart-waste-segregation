import torch
from torchvision.datasets import ImageFolder
from torchvision.transforms import transforms
from torch.utils.data import DataLoader




tfm = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=10),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

train_ds = ImageFolder(r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\train', transform=tfm)
#test_ds = ImageFolder(test_root, transform=tfm)

print(train_ds.class_to_idx)