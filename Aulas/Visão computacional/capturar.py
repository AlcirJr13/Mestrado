import time

import cv2

#Webcam
cap = cv2.VideoCapture(0)

for cont in range (0,20):
    time.sleep(1)
    ret, frame = cap.read()
    cv2.imwrite("imagens/"+str(cont+1)+".png",frame)

cap.release()
cv2.destroyAllWindows()
