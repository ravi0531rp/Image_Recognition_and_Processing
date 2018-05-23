import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\ImageRecPython\\new_images\\butterfly.jpg', cv2.IMREAD_COLOR)
# cv2.line(img, (0, 0), (150, 150), (255, 78, 0), 15)  # the last parameter is linewidh # random line
cv2.rectangle(img, (150, 25), (880, 680), (0, 255, 0), 5)
cv2.circle(img, (500, 370), 350, (255, 0, 0), 5)
pts = np.array([[100, 100], [200, 200], [300, 100], [400, 100]], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 0), 3)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'hey there',(100,130),font,5,(255,0,0),5)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.imshow(img, cmap='gray', interpolation='bicubic')  # it spits rgb
# plt.show()
# 160,32 860,660
