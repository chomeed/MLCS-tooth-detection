from mmdet.apis import init_detector, inference_detector
import json 


# Load the initialized detection model
config_file = 'configs/test_tooth_only.py'
checkpoint_file = 'mmdetection/experiments/tooth_only_2/epoch_20.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or 'cpu'
# Inference on an image
image = 'mmdetection/data/tooth_detection/sample/526950.JPG'
result = inference_detector(model, image)
# Unpack the result
#num_classes = model.CLASSES  # Total number of classes in the model
num_classes = 32
# Each element of 'result' corresponds to a class

labels = result.pred_instances.labels.tolist()
scores = result.pred_instances.scores.tolist()
bboxes = result.pred_instances.bboxes.tolist()

for bbox, score, label in zip(labels, scores, bboxes):
    print(bbox, score, label)

inferences = list(zip(scores, labels, bboxes))

from remove_duplicates import remove_duplicates_and_keep_highest 

filtered_inferences = remove_duplicates_and_keep_highest(inferences) 
for _ in filtered_inferences:
    print(_)

