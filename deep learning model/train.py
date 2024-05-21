import torch
from torch.nn import Linear, CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader

import torchvision
from torchvision.datasets import ImageFolder
from torchvision.models import resnet34
from torchvision.transforms import transforms

import os
from time import time
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Adjust paths based on your directory structure
train_root = r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\train'
test_root = r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\test'


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

len_train = len(train_ds)
len_test = len(test_ds)

train_loader = DataLoader(train_ds, batch_size=50, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=50, shuffle=True)

model = torchvision.models.resnet34(pretrained=True)
model.fc = Linear(in_features=512, out_features=len(train_ds.classes))
model = model.to(device)

optimizer = Adam(model.parameters(), lr=3e-4, weight_decay=0.0001)
loss_fn = CrossEntropyLoss()

for epoch in range(12):
    start = time()
    tr_acc = 0
    test_acc = 0

    # Train
    model.train()
    with tqdm(train_loader, unit="batch") as tepoch:
        for xtrain, ytrain in tepoch:
            optimizer.zero_grad()
            xtrain = xtrain.to(device)
            ytrain = ytrain.to(device)
            train_prob = model(xtrain)
            loss = loss_fn(train_prob, ytrain)
            loss.backward()
            optimizer.step()

            train_pred = torch.max(train_prob, 1).indices
            tr_acc += int(torch.sum(train_pred == ytrain))

        ep_tr_acc = tr_acc / len_train

    # Evaluate
    model.eval()
    with torch.no_grad():
        for xtest, ytest in test_loader:
            xtest = xtest.to(device)
            ytest = ytest.to(device)
            test_prob = model(xtest)
            test_pred = torch.max(test_prob, 1).indices
            test_acc += int(torch.sum(test_pred == ytest))

        ep_test_acc = test_acc / len_test

    end = time()
    duration = (end - start) / 60

    print(f"Epoch: {epoch}, Time: {duration}, Loss: {loss}\nTrain_acc: {ep_tr_acc}, Test_acc: {ep_test_acc}")

# Save the trained model
torch.save(model.state_dict(), '../Models/wastev7.pth')
