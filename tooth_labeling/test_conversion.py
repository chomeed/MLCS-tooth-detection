from pycocotools.coco import COCO
import json
from bbox2list import bbox2list
from category_id_conversion import match_template, id2tooth

# 데이터 불러오기
filepath = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/tooth_only.json' 
teeth_coco = COCO(annotation_file=filepath)

labels = ('upper', 'lower')

images_list = json.load(open(filepath))['images']

# upper나 lower인 이미지 ids 추출해서 리스트로 만들기 
new_images_id_list = []

for img in images_list: 
    for label in labels: 
        if label in img["file_name"]:
            new_images_id_list.append(img["id"])

# evaluate
correct = 0 
total = len(new_images_id_list)

for img_id in new_images_id_list: 
    anns_id = teeth_coco.getAnnIds(img_id)
    anns = teeth_coco.loadAnns(anns_id) 
    sorted_dets = bbox2list(anns) # list of dets 

    sorted_teeth = [] 
    for det in sorted_dets: 
        sorted_teeth.append(id2tooth[det['category_id']])

    correct += match_template(sorted_teeth)

print("correct:", correct)
print("total:", total)
print(f"accuracy: {correct/total}")
