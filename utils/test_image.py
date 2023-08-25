from mmdet.apis import init_detector, inference_detector
# Load the initialized detection model
config_file = 'configs/test_tooth_only.py'
checkpoint_file = 'mmdetection/experiments/tooth_only_2/epoch_20.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or 'cpu'
# Inference on an image
image = 'mmdetection/data/tooth_detection/test_sample/520928.JPG'
result = inference_detector(model, image)
# Unpack the result
#num_classes = model.CLASSES  # Total number of classes in the model
num_classes = 32
# Each element of 'result' corresponds to a class
#result.bboxes
#result.labels
#result.scores
#print(result)

#for k, v in result.pred_instances.items(): 
#    print(k, v)

#gt_filename = 'mmdetection/data/tooth_detection/annotations/tooth_only_v1/test.json'
#from mmdet.datasets.api_wrappers import COCO, COCOeval
#coco_api = COCO(gt_filename)


labels = result.pred_instances.labels.tolist()
scores = result.pred_instances.scores.tolist()
bboxes = result.pred_instances.bboxes.tolist()

for bbox, score, label in zip(labels, scores, bboxes):
    print(bbox, score, label)

l = list(zip(scores, labels, bboxes))

from remove_duplicates import remove_duplicates_highest_score 

l = remove_duplicates_highest_score(l) 
for _ in l:
    print(_)


#for class_id in range(num_classes):    
#    class_results = result[class_id]  # Detections for the current class
#    # 'class_results' is an array of shape (N, 5), where N is the number of detections    
#    # Each row contains [x_min, y_min, x_max, y_max, score] for a detected object
#    for bbox in class_results:
#        x_min, y_min, x_max, y_max, score = bbox
#        #class_name = model.CLASSES[class_id]  # Name of the current class
#        print(f"Class: {class_id}, BBox: [{x_min}, {y_min}, {x_max}, {y_max}], Score: {score}")
