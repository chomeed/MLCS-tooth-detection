Tasks to do: 
[x] use DNN to classify the orientation of the image(front, upper, lower, left, right) 
[ ] convert a series of teeth detections into an ordered array of tooth numbers 
[ ] in case of right, left, front intraoral images, split the upper and lower 
[ ] tooth similarity matrix 
[ ] slipping on FDI template 
[ ] evaluate on different models
- total number of available data

1. use DNN to classify the orientation of the image

Input: image rgb (3-dim)  
Label: class (front, left, right, upper, lower)

- data cleansing: sample.json 
- use ResNet34 
- probably need to resize 

Accuracy
without training: 25.02% 
Epoch 1: 99.75% 
Epoch 2: 99.79%
accuracy then decreased due to overfitting...

2. convert a series of teeth detections into an ordered array of tooth numbers 

Input: list of detections   
    category_id: tooth number 
    bbox: (x, y, w, h) --> (left corner coords, width, height) 
Output: (ordered from left to right) list of detections  
    e.g [18, 17, 16, 15, 14] or [41, 31, 32, 33] etc. 

using the center x coord of bboxes, sort them in ascending order
left <- smallest ... largest --> right

- unit test 
given two teeth, assert that they are in the correct order 
-> just for testing on ground truth 

MST ->