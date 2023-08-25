# post_process1.p y 
from mmdet.datasets.api_wrappers import COCO
from tdqm import tdqm 
from remove_duplicates import remove_duplicates_and_keep_highest 
import json 

# Prepare COCO dataset
gt_filename = 'mmdetection/data/tooth_detection/annotations/tooth_only_v1/test.json'
coco_api = COCO(gt_filename)
pbar = tdqm(coco_api.imgs)

# Load the initialized detection model
config_file = 'configs/test_tooth_only.py'
checkpoint_file = 'mmdetection/experiments/tooth_only_2/epoch_20.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or 'cpu'

# Accumulate all post processed inferences
post_processed = []


# Iterate over COCO dataset
for img in pbar: 
    # Inference 
    result = inference_detector(model, image)
    
    # Tensor to List conversion
    labels = result.pred_instances.labels.tolist()
    scores = result.pred_instances.scores.tolist()
    bboxes = result.pred_instances.bboxes.tolist()
    inferences = list(zip(scores, labels, bboxes))

    # remove duplicates → assign to ‘filtered inferences’
    filtered_inferences = remove_duplicates_and_keep_highest(inferences)
    post_processed.extend(filtered_inferences)
pbar.close()


# save to new json file 
with open('post_processed.json', 'w') as newfile:
    json.dump(post_processed, newfile)
