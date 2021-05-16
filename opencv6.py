import cv2
import numpy as np

image = np.full((512, 512, 3), 255, np.uint8)
# image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 3)
#
# image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 3)
#
# image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)
#
# points = np.array([[5, 5], [128, 258], [463, 444], [400, 150]])
# image = cv2.polylines(image, [points], True, (0, 0, 255), 4)
#
image = cv2.putText(image, "Hello World", (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

cv2.imshow("image", image)
cv2.waitKey(0)