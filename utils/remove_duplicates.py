def remove_duplicates_and_keep_highest(predictions, image_id=None):
    '''
    return : list of dictionaries (keys - image_id, score, bbox, category_id)
    '''
    unique_predictions = {}
    
    for score, category_id, bbox in predictions:
        if category_id in unique_predictions:
            if score > unique_predictions[category_id][0]:
                unique_predictions[category_id] = (score, bbox)
        else:
            unique_predictions[category_id] = (score, bbox)
    
    filtered_predictions = [{"image_id": image_id, "score": score, "category_id": category_id, "bbox": bbox} for category_id, (score, bbox) in unique_predictions.items()]
    
    # Sort the filtered predictions in descending order by score
    #filtered_predictions.sort(reverse=True)
    
    return filtered_predictions
