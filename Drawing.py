import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Robocon is Great!' , (200,height -10) ,font,1,(0,0,0), 5, cv2.LINE_AA )


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
