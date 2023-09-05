def bbox2list(dets):
    '''
    Input: list of detections(dict)   
        category_id: tooth number 
        bbox: (x, y, w, h) --> (left corner coords, width, height) 
    Output: (ordered from left to right) list of detections 
        same as input but in different order   
        e.g [18, 17, 16, 15, 14] or [41, 31, 32, 33] etc. 

    sort based on center x 
    -> corner x + half of width
    '''
    
    return sorted(dets, key=lambda d:d['bbox'][0] + d['bbox'][2] / 2)


# UNIT TEST
if __name__ == "__main__":
    from category_id_conversion import id2tooth
    sample_data = [ # lower dentition, 14 in total 
        {'bbox': [2647.3066860465115, 5.002178649237473, 600.5232558139537, 490.21350762527237], 'category_id': 24}, 
        {'bbox': [2517.1933139534885, 410.1786492374727, 555.484011627907, 625.2723311546843], 'category_id': 23}, 
        {'bbox': [2407.0973837209303, 980.4270152505447, 460.40116279069844, 380.16557734204787], 'category_id': 22}, 
        {'bbox': [2317.0188953488373, 1295.5642701525055, 385.3357558139537, 400.1742919389976], 'category_id': 21}, 
        {'bbox': [2176.8968023255816, 1630.7102396514156, 350.3052325581393, 355.15468409586106], 'category_id': 20}, 
        {'bbox': [1941.6918604651162, 1760.7668845315907, 295.2572674418609, 360.1568627450979], 'category_id': 19}, 
        {'bbox': [1671.456395348837, 1820.79302832244, 305.26598837209326, 370.1612200435734], 'category_id': 18}, 
        {'bbox': [1431.2470930232557, 1770.7712418300653, 295.25726744186045, 360.1568627450979], 'category_id': 26}, 
        {'bbox': [1110.968023255814, 1750.7625272331156, 325.2834302325582, 380.1655773420475], 'category_id': 27}, 
        {'bbox': [850.7412790697674, 1610.7015250544662, 350.3052325581393, 380.165577342048], 'category_id': 28}, 
        {'bbox': [615.5363372093022, 1300.566448801743, 425.3706395348838, 400.17429193899784], 'category_id': 29}, 
        {'bbox': [440.3837209302326, 980.4270152505447, 455.39680232558146, 385.1677559912854], 'category_id': 30}, 
        {'bbox': [285.24854651162786, 410.1786492374727, 600.5232558139536, 605.2636165577342], 'category_id': 31}, 
        {'bbox': [140.12209302325581, 0.0, 630.5494186046514, 425.1851851851852], 'category_id': 32}
    ] 

    sorted_sample_data = bbox2list(sample_data)
    sorted_teeth = [] 
    for det in sorted_sample_data: 
        sorted_teeth.append(id2tooth[det['category_id']])
    print(sorted_teeth)