# cspace.py
# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # define range of red color in HSV
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])

    # define range of green color in HSV
    lower_green = np.array([40,40,40])
    upper_green = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res_red = cv2.bitwise_and(frame,frame, mask= mask_red)
    res_green = cv2.bitwise_and(frame,frame, mask= mask_green)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((3,3), np.uint8) # Taking a matrix of size 5 as the kernel

    img_erosion_blue = cv2.erode(res, kernel,iterations = 2)
    img_dilation_blue = cv2.dilate(img_erosion_blue, kernel,iterations = 2)

    img_erosion_red = cv2.erode(res_red, kernel,iterations = 2)
    img_dilation_red = cv2.dilate(img_erosion_red, kernel,iterations = 2)

    img_erosion_green = cv2.erode(res_green, kernel,iterations = 2)
    img_dilation_green = cv2.dilate(img_erosion_green, kernel,iterations = 2)
    
    cv2.imshow('Original',frame)

    cv2.imshow('Blue',res)
    cv2.imshow('Red',res_red)
    cv2.imshow('Green',res_green)

    cv2.imshow('Mask Blue',mask)
    cv2.imshow('Mask Red',mask_red)
    cv2.imshow('Mask Green',mask_green)

    cv2.imshow('Erosion_RED', img_erosion_red)
    cv2.imshow('Dilation_RED', img_dilation_red)
    cv2.imshow('Erosion_BLUE', img_erosion_blue)
    cv2.imshow('Dilation_BLUE', img_dilation_blue)
    cv2.imshow('Erosion_GREEN', img_erosion_green)
    cv2.imshow('Dilation_GREEN', img_dilation_green)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
