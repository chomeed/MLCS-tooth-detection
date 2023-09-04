import torch 

def test(model, test_dataloader): 
    correct = 0
    total = 0

    with torch.no_grad():
        for i, (images, labels) in enumerate(test_dataloader): 
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    # Calculate and print the accuracy
    accuracy = 100 * correct / total
    print(f'Accuracy on the test dataset: {accuracy:.2f}%')
    return accuracy