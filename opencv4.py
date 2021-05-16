import cv2
import numpy as np

image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.imshow('image', thres1)
cv2.waitKey(0)

cv2.imshow('image', thres2)
cv2.waitKey(0)
