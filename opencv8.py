import cv2

image = cv2.imread("digit_image.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)

cv2.imshow("image", thresh)
cv2.waitKey(0)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

cv2.imshow("image", image)
cv2.waitKey(0)

contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imshow("image", image)
cv2.waitKey(0)

hull = cv2.convexHull(contour)
image = cv2.drawContours(image, [hull], -1, (255, 0, 0), 4)

cv2.imshow("image", image)
cv2.waitKey(0)
