from sklearn.model_selection import train_test_split
import json 

sample_file = 'sample_cleansed.json'
with open(sample_file, 'r') as rf: 
    data = json.load(rf) 

train, test = train_test_split(data, train_size=0.8, shuffle=True)

with open('train_cleansed.json', 'w') as wf: 
    json.dump(train, wf)

with open('test_cleansed.json', 'w') as wf: 
    json.dump(test, wf)   