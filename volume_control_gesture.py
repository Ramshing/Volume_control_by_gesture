from math import hypot

import cv2
import time
import numpy as np
import Hand_Tracking_module as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# defining the camera size
width_cam, height_cam = 1280,720

#defining the htm object
Detector=htm.HandDetector(detectionCon=0.7)

cap=cv2.VideoCapture(0)
cap.set(3,width_cam)
cap.set(4,height_cam)
p_time=0

# library for controlling PC volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volrange=volume.GetVolumeRange()
print(volume.GetVolumeRange())
minvol=volrange[0]
maxvol=volrange[1]
vol=0
volbar=400
volper=0

while True:
    SUCCESS, img=cap.read()
    img=Detector.FindHands(img)
    lmlist=Detector.FindPosition(img,draw=False)

    #getting the required landmark points
    if len(lmlist)!=0:
        #print(lmlist[4],lmlist[8])

        x1,y1 = lmlist[4][1], lmlist[4][2]
        x2,y2 = lmlist[8][1], lmlist[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),15,(69,0,259),cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (69, 0, 259), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
        cv2.circle(img,(cx,cy),15,(69,0,259),cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        print(length)

        #hand range (50,420)
        #vol range (-96,0)
        vol=np.interp(length,[50,300],[minvol,maxvol])
        volbar = np.interp(length, [50, 300], [400, 150])
        volper=np.interp(length, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img,(50,150),(85,400),(0,0,255),3)
    cv2.rectangle(img,(50,int(volbar)),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(img, f'Vol_Per:{int(volper)}%', (40, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)

    c_time=time.time()
    fps=1/(c_time-p_time)
    p_time=c_time

    cv2.putText(img,f'FPS:{int(fps)}',(30,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)