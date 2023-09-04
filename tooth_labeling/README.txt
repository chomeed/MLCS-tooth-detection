Tasks to do: 
- use DNN to classify the orientation of the image(front, upper, lower, left, right) 
- convert a series of teeth detections into an ordered array of tooth numbers 
- in case of right, left, front intraoral images, split the upper and lower 
- tooth similarity matrix 
- slipping on FDI template 
- evaluate on different models



1. use DNN to classify the orientation of the image

Input: image rgb (3-dim)  
Label: class (front, left, right, upper, lower)

- data cleansing: sample.json 
- use ResNet34 
- probably need to resize 