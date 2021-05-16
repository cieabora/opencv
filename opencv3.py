import cv2
import numpy as np

# 이미지 크기 줄이기
image = cv2.imread('image.jpg')
cv2.imshow('image', image)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
cv2.imshow('image', shrink)
cv2.waitKey(0)
cv2.imwrite("image1.jpg", shrink)

# 이미지 위치 변경
image = cv2.imread('image1.jpg')

height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))

cv2.imshow('image', dst)
cv2.waitKey(0)

# 이미지 회전
image = cv2.imread('image1.jpg')
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('image', dst)
cv2.waitKey(0)