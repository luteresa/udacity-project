# **Finding Lane Lines on the Road** 

---

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

## tools i will use

---

color selection, 

region of interest selection, 

grayscaling, 

Gaussian smoothing, 

Canny Edge Detection 
 
Hough Tranform line detection. 

---

### Reflection



### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. 

First, I converted the images to grayscale

Second, Canny Edge Detection 

third,  Hough Tranform  line detection

fourth,　draw lane line



In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]



### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...




### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...

pip install moviepy

ERROR: Cannot uninstall 'imageio'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

pip install moviepy --upgrade --ignore-install imageio
