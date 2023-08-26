def remove_duplicates_and_keep_highest(predictions, image_id=None):
    '''
    return : list of dictionaries (keys - image_id, score, bbox, category_id)
    '''
    predictions = []
    
    for category_id, score, bbox in predictions:

        if len(predictions) == 0: 
            predictions.append((category_id, score, bbox)) 
            continue 
        
        overlapped = False
        for idx, (category_id2, score2, bbox2) in enumerate(predictions): 
            iou = compute(bbox, bbox2) 
            if iou > 0.6: 
                overlapped = True
                # compare score 
                if score > score2: # 현재 인스턴스가 더 높은 점수를 가지고 있다면, 바꾸기 
                    predictions[idx] = (category_id, score, bbox)
        
        if overlapped == False:
            predictions.append((category_id, score, bbox)) 
    
    filtered_predictions = [{"image_id": image_id, "score": score, "category_id": category_id, "bbox": bbox} for (category_id, score, bbox) in predictions]
    
    return filtered_predictions


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