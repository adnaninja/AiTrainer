import cv2
import numpy as np
import time
import poseModule as pm

cap = cv2.VideoCapture(1)
detector = pm.poseDetector()
count = 0
dirction = 0
pTime = 0
bar = 0
percent = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 3)
    img = cv2.resize(img, (1280,720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        #left arm
        #detector.findAngel(img, 12, 14, 16)
        # right arm
        angle = detector.findAngel(img, 11, 13, 15)
        percent = np.interp(angle, (205,300), (0,100))
        bar = np.interp(angle, (205,300), (650,100))
        print(angle, percent)

        # check the dumbbell curls
        if percent == 100:
            if dirction == 0:
                count += 0.5
                dirction = 1
        if percent == 0:
            if dirction == 1:
                count += 0.5
                dirction = 0

        print(count)

    cv2.rectangle(img, (1100, 100), (1175, 650), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (1100, int(bar)), (1175, 650), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(percent)} % ', (1100, 75), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4)

    cv2.rectangle(img, (0,450), (250,720), (0,255,0),cv2.FILLED)

        #print(count)
    cv2.putText(img, f'{count}', (45,670), cv2.FONT_HERSHEY_COMPLEX,2, (255,0,0), 5)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    print(count)


    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 5)




    cv2.imshow('Ai Adnan trainar', img)
    cv2.waitKey(1)

