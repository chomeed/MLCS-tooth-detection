import torch
from torchvision import transforms
from models import resnet34
from datasets import ToothImageDataset
from torch.utils.data import DataLoader

from test import test

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

train_img_label_file = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/train_cleansed.json'
test_img_label_file = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/test_cleansed.json'

img_dir = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/sample'

train_dataset = ToothImageDataset(img_label_file=train_img_label_file, img_dir=img_dir, transform=transform)
test_dataset = ToothImageDataset(img_label_file=test_img_label_file, img_dir=img_dir, transform=transform)

print("number of train img-label pairs: ", len(train_dataset))
print("number of test img-label pairs: ", len(test_dataset))

train_dataloader = DataLoader(dataset=train_dataset, batch_size=2, shuffle=True)
test_dataloader = DataLoader(dataset=test_dataset, batch_size=2, shuffle=True)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = resnet34.to(device)

optimizer = torch.optim.Adam(params=model.parameters(), lr=0.001, betas=[0.9, 0.999], eps=1e-8, weight_decay=0)
criterion = torch.nn.CrossEntropyLoss()
num_epochs = 10 

test(model, test_dataloader, device)
for e in range(1, num_epochs+1): 
    for i, (images, labels) in enumerate(train_dataloader):
        images, labels = images.to(device), labels.to(device)

        # Zero the gradient buffers
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(images)
        
        # Compute the loss
        loss = criterion(outputs, labels)

        # Backpropagation and optimization
        loss.backward()
        optimizer.step()

        if (i+1) % 20 == 0:
            print(f'Epoch [{e+1}/{num_epochs}], Step [{i+1}/{len(train_dataloader)}], Loss: {loss.item():.6f}')
    
    acc = test(model, test_dataloader, device)
    # Save the trained model
    torch.save(model.state_dict(), f'epoch_{e}.pth')

