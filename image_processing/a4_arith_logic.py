import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('F:\\ImageRecPython\\new_images\\3D-Matplotlib.png')
img2 = cv2.imread('F:\\ImageRecPython\\new_images\\mainsvmimage.png')
img3 = cv2.imread('F:\\ImageRecPython\\new_images\\mainlogo.png')
# add = img1+img2
# add = cv2.add(img1, img2)  # simple pixel to pixel value addition
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# cv2.imshow('add', weighted)
cv2.imshow('logo', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
