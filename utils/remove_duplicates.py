def remove_duplicates_and_keep_highest(predictions):
    unique_predictions = {}
    
    for score, label, bboxes in predictions:
        if label in unique_predictions:
            if score > unique_predictions[label][0]:
                unique_predictions[label] = (score, bboxes)
        else:
            unique_predictions[label] = (score, bboxes)
    
    filtered_predictions = [(score, label, bboxes) for label, (score, bboxes) in unique_predictions.items()]
    
    # Sort the filtered predictions in descending order by score
    filtered_predictions.sort(reverse=True)
    
    return filtered_predictions