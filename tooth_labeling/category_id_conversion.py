id2tooth = {
    2: 11,
    3: 12, 
    4: 13,
    5: 14, 
    6: 15,
    7: 16,
    8: 17,
    9: 18, 
    10: 21,
    11: 22, 
    12: 23,
    13: 24,
    14: 25, 
    15: 26,
    16: 27, 
    17: 28, 
    18: 31,
    19: 32,
    20: 33,
    21: 34,
    22: 35,
    23: 36,
    24: 37,
    25: 38,
    26: 41,
    27: 42,
    28: 43, 
    29: 44, 
    30: 45,
    31: 46,
    32: 47,
    33: 48
}

upper_template = [18, 17, 16, 15, 14, 13, 12, 11, 21, 22, 23, 24, 25, 26, 27, 28]
lower_template = [48, 47, 46, 45, 44, 43, 42, 41, 31, 32, 33, 34, 35, 36, 37, 38]

def match_template(teeth_list):
    match = False
    if is_list_found_in_order(upper_template, teeth_list):
        match = True 
    if is_list_found_in_order(lower_template, teeth_list):
        match = True
    return match

def is_list_found_in_order(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    
    for i in range(len1 - len2 + 1):
        if list1[i:i+len2] == list2:
            return True
    
    return False


# UNIT TEST 
if __name__ == "__main__":
    print(len(id2tooth))
    my_teeth = [31, 32, 3]
    print(match_template(my_teeth))
    