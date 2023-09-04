import torch
from torchvision import transforms
from models import resnet34
from datasets import ToothImageDataset
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

img_label_file = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/sample_cleansed.json'
img_dir = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/sample'

dataset = ToothImageDataset(img_label_file=img_label_file, img_dir=img_dir, transform=transform)
dataloader = DataLoader(dataset=dataset, batch_size=2, shuffle=True)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = resnet34

optimizer = torch.optim.SGD(params=model.parameters(), lr=0.005, momentum=0.9)
criterion = torch.nn.CrossEntropyLoss()
num_epochs = 10 

for e in range(num_epochs): 
    for i, (images, labels) in enumerate(dataloader):
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
        
        if (i+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

# Save the trained model
torch.save(model.state_dict(), 'resnet34.pth')