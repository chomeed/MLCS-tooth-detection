from mmengine.structures import InstanceData
from mmdet.structures import DetDataSample
from mmdet.visualization import DetLocalVisualizer

def visualize_image(image, inferences):
    # inferences - list of dicts(image_id, category_id, bbox, score)
    labels = [d['category_id'] for d in inferences]
    scores = [d['score'] for d in inferences]
    bboxes = [d['bbox'] for d in inferences]

    det_instances = InstanceData()
    det_instances.labels = labels
    det_instances.scores = scores
    det_instances.bboxes = bboxes

    det_data_sample = DetDataSample()
    det_data_sample.pred_instances = det_instances

    det_local_visualizer = DetLocalVisualizer()
    det_local_visualizer.add_datasample('image', image, det_data_sample, out_file='test_visualize.jpg')



