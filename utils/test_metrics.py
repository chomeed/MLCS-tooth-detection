from mmdet.datasets.api_wrappers import COCO, COCOeval
import numpy as np 
from collections import OrderedDict
import itertools
from terminaltables import AsciiTable

metainfo = {
    'classes': ('Tooth num 21', 'Tooth num 22', 'Tooth num 23', 
                'Tooth num 24', 'Tooth num 25', 'Tooth num 26', 'Tooth num 27', 
                'Tooth num 28', 'Tooth num 31', 'Tooth num 32', 'Tooth num 11', 
                'Tooth num 33', 'Tooth num 34', 'Tooth num 35', 'Tooth num 36', 
                'Tooth num 37', 'Tooth num 38', 'Tooth num 41', 'Tooth num 42', 
                'Tooth num 43', 'Tooth num 44', 'Tooth num 12', 'Tooth num 45', 
                'Tooth num 46', 'Tooth num 47', 'Tooth num 48', 'Tooth num 13', 
                'Tooth num 14', 'Tooth num 15', 'Tooth num 16', 'Tooth num 17', 'Tooth num 18'),
    'palette': [(119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228), 
                (0, 60, 100), (0, 80, 100), (0, 0, 70), (0, 0, 192), (250, 170, 30), 
                (100, 170, 30), (220, 220, 0), (175, 116, 175), (250, 0, 30), 
                (165, 42, 42), (255, 77, 255), (0, 226, 252), (182, 182, 255), 
                (0, 82, 0), (120, 166, 157), (110, 76, 0), (174, 57, 255), (199, 100, 0), 
                (72, 0, 118), (255, 179, 240), (0, 125, 92), (209, 0, 151), 
                (0, 228, 0), (255, 208, 186), (197, 226, 255), 
                (171, 134, 1), (109, 63, 54), (207, 138, 255)]
}

gt_filename = 'mmdetection/data/tooth_detection/annotations/tooth_only_v1/test.json'
#pred_filename = 'work_dirs/test_results/first_test.bbox.json'
pred_filename = 'post_processed_iou.json'
coco_api = COCO(gt_filename)
coco_dt = coco_api.loadRes(pred_filename)

coco_eval = COCOeval(coco_api, coco_dt, 'bbox')
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()

# output sample 
# Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.663
# Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.849
# Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.787
# ... 

cat_ids = coco_api.get_cat_ids(cat_names=metainfo['classes'])
coco_eval.params.catIds = cat_ids

eval_results = OrderedDict()

# Compute per-category AP
# from https://github.com/facebookresearch/detectron2/
precisions = coco_eval.eval['precision']
# precision: (iou, recall, cls, area range, max dets)
assert len(cat_ids) == precisions.shape[2]

results_per_category = []
for idx, cat_id in enumerate(cat_ids):
    t = []
    # area range index 0: all area ranges
    # max dets index -1: typically 100 per image
    nm = coco_api.loadCats(cat_id)[0]
    precision = precisions[:, :, idx, 0, -1]
    precision = precision[precision > -1]
    if precision.size:
        ap = np.mean(precision)
    else:
        ap = float('nan')
    t.append(f'{nm["name"]}')
    t.append(f'{round(ap, 3)}')
    eval_results[f'{nm["name"]}_precision'] = round(ap, 3)

    # indexes of IoU  @50 and @75
    for iou in [0, 5]:
        precision = precisions[iou, :, idx, 0, -1]
        precision = precision[precision > -1]
        if precision.size:
            ap = np.mean(precision)
        else:
            ap = float('nan')
        t.append(f'{round(ap, 3)}')

    # indexes of area of small, median and large
    for area in [1, 2, 3]:
        precision = precisions[:, :, idx, area, -1]
        precision = precision[precision > -1]
        if precision.size:
            ap = np.mean(precision)
        else:
            ap = float('nan')
        t.append(f'{round(ap, 3)}')
    results_per_category.append(tuple(t))

num_columns = len(results_per_category[0])
results_flatten = list(
    itertools.chain(*results_per_category))
headers = [
    'category', 'mAP', 'mAP_50', 'mAP_75', 'mAP_s',
    'mAP_m', 'mAP_l'
]
results_2d = itertools.zip_longest(*[
    results_flatten[i::num_columns]
    for i in range(num_columns)
])
table_data = [headers]
table_data += [result for result in results_2d]
table = AsciiTable(table_data)
print('\n' + table.table)
print(table)
print(table_data)

import json

def list_to_json(input_list):
    headers = input_list[0]
    json_data = []

    for values in input_list[1:]:
        category_data = {}
        for i, header in enumerate(headers):
            category_data[header] = values[i]
        json_data.append(category_data)

    return json_data

with open('test_json.json', 'w') as wf:
    json.dump(list_to_json(table_data), wf)