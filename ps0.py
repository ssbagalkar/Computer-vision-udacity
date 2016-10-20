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
import numpy
import os
from matplotlib import pyplot as plt

# 2.part a

img1 = cv2.imread('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output\ps0-1-a-1.png')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img1)
cv2.waitKey(0)


# Extract the red and blue channels
blue = img1[:,:,0]
red = img1[:,:,2]

#Manual : swap the channels
img1[:,:,0] = red
img1[:,:,2] = blue
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img1)
cv2.waitKey(0)

#save the modified file to the directory



# Automated using built in function
img_auto = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img_auto)
cv2.waitKey(0)

os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-a-1.png',img_auto)

# 2.part b
img_mono_green = img1[:,:,1]
cv2.imshow('image',img_mono_green)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-b-1.png',img_mono_green)

#2.part c
img_mono_red = img1[:,:,2]
cv2.imshow('image',img_mono_red)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-2-c-1.png',img_mono_red)

#part 3
#convert to grayscale
img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img_gray)
height,width = img_gray.shape

#replace centre 100x100 pixels
centre_pixels = img_gray[206:305,206:305]
img2 = cv2.imread('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output\ps0-1-a-2.png')
img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img2_gray[206:305,206:305] = centre_pixels
cv2.imshow('image',img2_gray)
cv2.waitKey(0)
os.chdir('C:\Intro to computer vision\Computer-vision-udacity\ps0_python\Output')
cv2.imwrite('ps0-3-a-1.png',img2_gray)



#part 4
