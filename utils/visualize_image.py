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

    det_instances.bboxes = xywh2xyxy(bboxes)

    det_data_sample = DetDataSample()
    det_data_sample.pred_instances = det_instances

    det_local_visualizer = DetLocalVisualizer()
    det_local_visualizer.add_datasample('image', image, det_data_sample, out_file='test_visualize.jpg')


if __name__ == '__main__': 
    import json 
    data = json.load(open('post_processed_p.json'))
    inferences = []
    for d in data:
        if d['image_id'] == 526950:
            inferences.append(d)

    print(len(inferences))

    import mmcv 
    image = mmcv.imread('test.jpg')
    visualize_image(image, inferences)