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
    det_instances.bboxes = torch.tensor(bboxes)

    det_data_sample = DetDataSample()
    det_data_sample.pred_instances = det_instances

    det_local_visualizer = DetLocalVisualizer()
    det_local_visualizer.add_datasample('image', image, det_data_sample, out_file='test_visualize.jpg')



