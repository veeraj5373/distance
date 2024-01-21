import numpy as np
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap =cv2.VideoCapture(0)
detector= FaceMeshDetector(maxFaces=1)
while True:
    success, img= cap.read()
    img , faces =detector.findFaceMesh(img,draw=None)


    if faces:
        face = faces[0]
        pointleft =face[145]
        pointright =face[374]


        cv2.line(img, pointleft,pointright,(0,200,0),3)
        cv2.circle(img,pointleft,5,(255,0,255),cv2.FILLED)
        cv2.circle(img,pointright,5,(255,0,255),cv2.FILLED)
        w,_ = detector.findDistance(pointleft,pointright)
        W=6.3
        w=w/100
        f=10.2
        d=(W*f)/w
        

        cvzone.putTextRect(img,f"Depth :{int(d)}cm",(face[10][0]-200,face[10][1]-50))




    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

