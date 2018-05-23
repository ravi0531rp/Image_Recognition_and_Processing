import numpy as np
import cv2

img = cv2.imread('F:\\ImageRecPython\\images\\low_contrast_1.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

brightness = 50

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = a + brightness
        if b > 255:
            b = 255
        img.itemset((i, j), b)

cv2.imwrite('F:\\ImageRecPython\\images\\brightness.jpg', img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
