# **Finding Lane Lines on the Road** 

---

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


## tools i will use

color selection, 

region of interest selection, 

grayscaling, 

Gaussian smoothing, 

Canny Edge Detection 
 
Hough Tranform line detection. 

---

### Reflection



### 1. Describe about the pipeline. 

My pipeline consisted of 5 steps. 

First, I converted the images to grayscale

Second, gaussian blue for image

third, Canny Edge Detection 

fourth, define a polygon to mask

fifh,  Hough Tranform  line detection

sixth,　draw lane line

### As part of the description, explain how you modified the draw_lines() function.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by lines_classify2()

in lines_classify2(img,lines), i follow steps below:

step 1:classify lines by the sign of line's slope(for left lines and right lines);

step 2: calclulate average slope of left_line and right_line;

step 3: filter some error slope;

step 4:calcluate average slope again(removed error slope);

step 5:calcluate left_bottom point of left_line and right_bottom point of right_line

at last, draw two lines(left_lien and right_line)



### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming is that the lane line detection is inaccurate when the vehicle turn around;

Another shortcoming could be that the lane line detection  miss when the segment is too short;




### 3. Suggest possible improvements to your pipeline

A possible improvement would be to update the draw_lines()


