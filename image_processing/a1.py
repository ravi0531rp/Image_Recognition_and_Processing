import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\ImageRecPython\\new_images\\low_contrast_1.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img,cmap='gray',interpolation='bicubic')           #it spits rgb
#plt.plot([50,100],[80,100],'c',linewidth=5) # c for color
plt.show()
cv2.imwrite('F:\\ImageRecPython\\new_images\\new_low_contrast.jpg',img)