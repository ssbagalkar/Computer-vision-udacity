# This code is the first assignment ps0

# Instructions :
# Color  planes:
# Swap the red and blue pixels of image 1
# Output: Store as ps0-2-a-1.png in the output folder
# Create a monochrome image (img1_green) by selecting the green channel of image 1
# Output: ps0-2-b-1.png
# Create a monochrome image (img1_red) by selecting the red channel of image 1
# Output: ps0-2-c-1.png
# Would you expect a computer vision algorithm to work on one better than the other?
# Output: Text response in report ps0_report.pdf

# Let's begin

#import all necessary modules
import cv2
import numpy as np
from scipy import signal
import os
from matplotlib import pyplot as plt

# 2.part a

img1 = cv2.imread('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output\ps0-1-a-1.png')
cv2.imshow('img1',img1)
cv2.waitKey(0)


# Extract the red and blue channels
blue = img1[:,:,0]
red = img1[:,:,2]

#Manual : swap the channels
img1[:,:,0] = red
img1[:,:,2] = blue
cv2.imshow('img1',img1)
cv2.waitKey(0)

#save the modified file to the directory



# Automated using built in function
img_auto = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
cv2.imshow('img_auto',img_auto)
cv2.waitKey(0)

os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-a-1.png',img_auto)

# 2.part b
img_mono_green = img1[:,:,1]
cv2.imshow('img_mono_green',img_mono_green)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-b-1.png',img_mono_green)

#2.part c
img_mono_red = img1[:,:,2]
cv2.imshow('img_mono_red',img_mono_red)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-c-1.png',img_mono_red)

#part 3
#convert to grayscale
img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray',img_gray)
height,width = img_gray.shape

#replace centre 100x100 pixels
centre_pixels = img_gray[206:305,206:305]
img2 = cv2.imread('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output\ps0-1-a-2.png')
img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2_gray[206:305,206:305] = centre_pixels
cv2.imshow('img2_gray',img2_gray)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-3-a-1.png',img2_gray)





#part 4
max_img1_green = img_mono_green.max()
min_img1_green = img_mono_green.min()
print "The max is %d and min is %d"%(max_img1_green,min_img1_green)

#Using built in
(minVal,maxVal,minLoc,maxLoc) = cv2.minMaxLoc(img_mono_green)
print "The automax is %d and automin is %d ."%(maxVal,minVal)

##Subtract the mean,then divide by standard devaiation ,then multiply by 10 and finally add the mean back in
img_math = cv2.absdiff(img_mono_green,img_mono_green.mean())
img_math = cv2.divide(img_mono_green,img_math.std())
img_math = cv2.multiply(img_math,10)
img_math = cv2.add (img_math,img_math.mean())
cv2.imshow('img_math',img_math)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-4-b-1.png',img_math)
cv2.destroyAllWindows()


# part 4 c
kernel = np.zeros((3,3),np.float32)
kernel[1,0] = 1
shift_img = signal.convolve2d(img_gray,kernel,mode='same')
shift_img = cv2.divide(shift_img,255)
cv2.imshow('shift_img',shift_img)
cv2.waitKey(0)


