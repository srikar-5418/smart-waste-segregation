import torch
from torchvision.datasets import ImageFolder
from torchvision.transforms import transforms
from torch.utils.data import DataLoader


def get_data_loaders(train_root, test_root, batch_size):
    # Define data transformations for data augmentation and normalization
    tfm = transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=10),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    train_ds = ImageFolder(train_root, transform=tfm)
    test_ds = ImageFolder(test_root, transform=tfm)

    print(train_ds.class_to_idx)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=True)

    return train_loader, test_loader
