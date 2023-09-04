from torch.utils.data import Dataset
import json 
from PIL import Image
#from torchvision.io import read_image
import os 

'''

self.img_labels 
list of { 
            filepath: str, 
            label:  str
        } 
->  
[ 
    (filepath1, label1), 
    (filepath2, label2), 
    ... 
]

'''

class ToothImageDataset(Dataset): 
    def __init__(self, img_label_file, img_dir='sample', transform=None, target_transform=None):
        with open(img_label_file, 'r') as rf: 
            data = json.load(rf) 
        
        self.img_labels = dict2tup(data)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
        pass 

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        filepath, label = self.img_labels[idx]
        full_filepath = os.path.join(self.img_dir, filepath) 
        #image = read_image(full_filepath) 
        image = Image.open(full_filepath)

        if self.transform: 
            image = self.transform(image) 
        if self.target_transform:
            label = self.target_transform(label)

        return image, label  

def dict2tup(l_of_d):
    l_of_t = []
    for d in l_of_d: 
        t = tuple(d.values())
        l_of_t.append(t)
    return l_of_t

        

# UNIT TEST
if __name__ == '__main__':
    dataset = ToothImageDataset(img_label_file='sample_cleansed.json', img_dir='sample')
    print(len(dataset))
    print(dataset[1])