import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('F:\\ImageRecPython\\new_images\\lion.jpg', cv2.IMREAD_COLOR)
px = img[55, 55]
print(px)
# ROI -> region of image
roi = img[100:150, 200:250]
# print(roi)
img[100:400, 200:300] = [255, 255, 255]

watch_face = img[20:100, 300:400]
img[0:80, 0:100] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
