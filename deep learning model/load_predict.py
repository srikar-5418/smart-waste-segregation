import numpy as np
import torch
from PIL._imaging import display
from torchvision.transforms import transforms
import torchvision.models as models
from torch.nn import Linear
from PIL import Image
import serial

ser=serial.Serial()
ser.port='COM7'
ser.close()
ser.open()
ser.baudrate=9600

# Define device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define transformations for input images
tfm = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Load the trained model
model = models.resnet34(pretrained=True)
model.fc=Linear(in_features=512,out_features=6)
model.load_state_dict(torch.load(r'C:\Users\karth\PycharmProjects\Epitome Prj\Models\wastev7.pth'))
model.eval()
model.to(device)

s1=r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\IMG\26.jpg'
s2=r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\IMG\2.jpg'
s3=r'C:\Users\karth\PycharmProjects\Epitome Prj\datasets\IMG\3.jpg'
sample_list = [s1]

for image_path in sample_list:
    img = Image.open(image_path)
    img.resize((224, 224)).show()
    img_tensor = tfm(img)
    img_tensor = img_tensor[np.newaxis, :]
    img_tensor = img_tensor.to(device)
    pred_prob = model(img_tensor)
    pred = torch.max(pred_prob, 1).indices
    pred = pred.item()
    if pred == 0:
        print(f"Model prediction {pred}, --ewaste")
    elif pred == 1:
        print(f"Model prediction {pred}, --food_waste")
    elif pred == 2:
        print(f"Model prediction {pred}, --leaf waste")
    elif pred == 3:
        print(f"Model prediction {pred}, --medical waste")
    elif pred == 4:
        print(f"Model prediction {pred}, --metal")
    elif pred == 5:
        print(f"Model prediction {pred}, --plastic")
    print("========================================================")
ser.write(str.encode(str(pred)))
ser.close()
