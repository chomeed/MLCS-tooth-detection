import json 

'''
Data cleansing 

COCO dataset -> {
                    filepath: filepath,
                    label: label_id
                }


label is one of ('left': 0, 'right': 1, 'front': 2, 'upper': 3, 'lower': 4) 

'''

def data_cleanse(annotations_file='sample.json', new_file='sample_cleansed.json'):
    # read images from json file 
    with open(annotations_file, 'r') as rf:
        data = json.load(rf)
    
    image_data = data['images'] # list of dicts --> {file_name, width, height, id} 
    
    img_labels = []

    # iterate over images 
    for img in image_data: 
        file_name = img['file_name']
        label = extract_label_id(file_name)
        if label:
            img_labels.append({"file_path": file_name, "label": label})
        else: 
            continue


    with open(new_file, 'w') as wf:
        json.dump(img_labels, wf, indent=4)
        

def extract_label_id(file_name):
    labels = {'left': 0, 'right': 1, 'front': 2, 'upper': 3, 'lower': 4}
    for label, id in labels.items(): 
        if label in file_name: 
            return id 
    return False


# UNIT TEST 
if __name__ == '__main__':
    #annotations_file = 'sample_unit_test.json'
    annotations_file = 'sample.json'
    data_cleanse(annotations_file)