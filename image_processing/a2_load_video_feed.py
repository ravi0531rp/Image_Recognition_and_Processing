import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()  # true/false , the feed
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)  # writing out
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break # break out

cap.release()
out.release()
cv2.destroyAllWindows()
