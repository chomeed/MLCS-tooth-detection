from sklearn.model_selection import train_test_split
import json 

root = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/'
sample_file = root + 'sample_cleansed.json'
with open(sample_file, 'r') as rf: 
    data = json.load(rf) 

train, test = train_test_split(data, train_size=0.8, shuffle=True)

with open(root + 'train_cleansed.json', 'w') as wf: 
    json.dump(train, wf)

with open(root + 'test_cleansed.json', 'w') as wf: 
    json.dump(test, wf)   