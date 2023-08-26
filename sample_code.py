def calculate_iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    intersection_x = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    intersection_y = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = intersection_x * intersection_y

    area_box1 = w1 * h1
    area_box2 = w2 * h2
    union_area = area_box1 + area_box2 - intersection_area

    iou = intersection_area / union_area
    return iou

# Example usage
gt_bbox = [10, 10, 20, 20]  # [x, y, width, height]
pred_bbox = [15, 15, 18, 18]

iou = calculate_iou(gt_bbox, pred_bbox)
print("IoU:", iou)

