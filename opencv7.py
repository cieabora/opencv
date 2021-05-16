import cv2

image = cv2.imread("image1.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow("image", thresh)
cv2.waitKey(0)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

cv2.imshow("image", image)
cv2.waitKey(0)

