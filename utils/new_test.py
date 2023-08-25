import mmcv
from mmdet.apis import init_detector, inference_detector
from mmdet.datasets import build_dataset
from mmdet.datasets.coco import CocoDataset
from mmdet.datasets import to_coco_json

# Load the config and checkpoint
config_file = 'configs/test_tooth_only.py'
checkpoint_file = 'mmdetection/experiments/tooth_only_2/epoch_20.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# Load the COCO dataset
data_root = 'mmdetection/data/tooth_detection/sample'  # Path to the root directory of the COCO dataset
ann_file = 'mmdetection/data/tooth_detection/annotations/tooth_only_v1/test.json'
dataset = build_dataset(dict(ann_file=ann_file, img_prefix=data_root))

# Load your post-processed results from the JSON file
with open('/work_dirs/test_results/first_test.bbox.json', 'r') as file:
    results = json.load(file)

# Convert results to COCO-style format
coco_results = to_coco_json(dataset, results)

# Use the COCO evaluation tools to calculate mAP
coco_eval = mmcv.runner.coco_eval.COCOEval(dataset.coco, coco_results, 'bbox')
coco_eval.params.img_ids = dataset.coco.get_img_ids()
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

# Print class-wise AP
classwise_aps = coco_eval.get_classwise_aps()
for class_id, ap in enumerate(classwise_aps):
    class_name = dataset.CLASSES[class_id]
    print(f"Class: {class_name}, AP: {ap:.4f}")
