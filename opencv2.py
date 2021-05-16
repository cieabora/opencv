# import cv2
# import time
# image = cv2.imread('image.jpg')
#
# print(image.shape)
# print(image.size)
#
# px = image[100, 100]
#
# print(px)
# print(px[2])
#
# # sol1
# start_time = time.time()
# for i in range(0, 100):
#     for j in range(100):
#         image[i, j] = [255, 255, 255]
# print(f'{time.time() - start_time} seconds')
#
# # sol2
# start_time = time.time()
# image[0:100, 0:100] = [0, 0, 0]
# print(f'{time.time() - start_time} seconds')
#
# cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('show', image)
# cv2.waitKey(0)
#
# # ROI 추출 및 복사
# roi = image[200:350, 50:200]
#
# image[0:150, 0:150] = roi
#
# cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('image', image)
# cv2.waitKey(0)
#
# # 특정한 색만 바꾸기
# image[:, :, 2] = 0
# cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('image', image)
# cv2.waitKey(0)
