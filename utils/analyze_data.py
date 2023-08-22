import json 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=True, help='name of the COCO json file')
args = parser.parse_args()

filename = args.filename

with open(filename, 'r') as file: 
    data = json.load(file)

images = data['images']
annotations = data['annotations']
categories = data['categories']

ann_list = [0] * (len(categories) + 1)
for ann in annotations:
    cat = int(ann["category_id"])
    ann_list[cat] += 1

print(f"\n\nTotal number of images: {len(images)}")
print(f"Total number of annotations: {len(annotations)}")
print(f"Total number of categories: {len(categories)}\n\n")

print("Class name -- ID -- Annotations")
for c in categories:
    print(c["name"], ':', c["id"], ':', ann_list[c["id"]])
print("\n\n")




