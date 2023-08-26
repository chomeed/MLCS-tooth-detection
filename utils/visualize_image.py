from mmengine.structures import InstanceData
from mmdet.structures import DetDataSample
from mmdet.visualization import DetLocalVisualizer
import torch

def visualize_image(image, inferences):
    # inferences - list of dicts(image_id, category_id, bbox, score)
    labels = [d['category_id'] for d in inferences]
    scores = [d['score'] for d in inferences]
    bboxes = [d['bbox'] for d in inferences]

    det_instances = InstanceData()
    det_instances.labels = torch.tensor(labels)
    det_instances.scores = torch.tensor(scores)
    bboxes = torch.tensor(bboxes)

    # xywh2xyxy
    bboxes[:, 2] += bboxes[:, 0]
    bboxes[:, 3] += bboxes[:, 1]

    det_instances.bboxes = bboxes

    det_data_sample = DetDataSample()
    det_data_sample.pred_instances = det_instances

    det_local_visualizer = DetLocalVisualizer()
    det_local_visualizer.add_datasample('image', image, det_data_sample, out_file='test_visualize.jpg')


if __name__ == '__main__': 
    import json 

    # find image id 
    image_id = None 
    sample = json.load(open('mmdetection/data/tooth_detection/annotations/tooth_only_v1/test.json'))
    for s in sample['images']:
        if s['file_name'] == '520051.JPG':
            image_id = s['id']
            print(image_id)
            

    file_path = 'mmdetection/data/tooth_detection/sample/520051.JPG'

    data = json.load(open('post_processed_iou.json'))
    inferences = []
    for d in data:
        if d['image_id'] == image_id:
            inferences.append(d)

    print(len(inferences))

    import mmcv 
    image = mmcv.imread(file_path)
    image = mmcv.bgr2rgb(image)
    visualize_image(image, inferences)
