from pycocotools.coco import COCO
import json
from bbox2list import bbox2list
from category_id_conversion import match_template, id2tooth

'''
correct: 5030
total: 6985
accuracy: 0.7201145311381532
'''

# 데이터 불러오기
filepath = '/home/summer23_intern1/workspace/MLCS-tooth-detection/mmdetection/data/tooth_detection/annotations/tooth_only_clean.json' 
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

incorrect = []

for img_id in new_images_id_list: 
    anns_id = teeth_coco.getAnnIds(img_id)
    anns = teeth_coco.loadAnns(anns_id) 
    sorted_dets = bbox2list(anns) # list of dets 

    sorted_teeth = [] 
    for det in sorted_dets: 
        sorted_teeth.append(id2tooth[det['category_id']])

    correct += match_template(sorted_teeth)

    if match_template(sorted_teeth) == False: 
        incorrect.append(img_id)
    if len(incorrect) == 3: break


print("correct:", correct)
print("total:", total)
print(f"accuracy: {correct/total}")
print("incorrect dets:")
for img in teeth_coco.loadImgs(incorrect):
    print(img["file_name"])
    