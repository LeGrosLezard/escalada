import cv2
import os
import numpy as np



from path import wall_save as ws
from path import wall_pieces as wp
from path import wall_no_pieces as wnp

from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture

#abs wall
#abs piece

#detection
#stp neo

def nothing(x):
    pass

##cv2.namedWindow("Tracking")
##cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
##cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
##cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
##cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
##cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
##cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


liste = os.listdir(wp)
R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE

position = []
for i in liste:


    img = open_picture(wp+i)
    img = cv2.resize(img, (500, 500))
    height, width, channel = img.shape
    img = img[70:height-50, 0:width]

    copy = img.copy()

    show_picture("img", img, 0, "")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #haut
    l_b = np.array([0, 0, 0])
    u_b = np.array([75, 255, 255])
    mask = cv2.inRange(hsv, l_b, u_b)

    blanck = blanck_picture(img);

    contours, _ = cv2.findContours(mask, R, P)

    maxi = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > maxi:
            maxi = cv2.contourArea(cnt)

    save = 0
    for cnts in contours:
        if cv2.contourArea(cnts) > 10 and\
           cv2.contourArea(cnts) < 1000:

            cv2.drawContours(blanck,[cnts],-1,(255,255,255), 1)
            cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))

            (x,y,w,h) = cv2.boundingRect(cnts)
            position.append([x, y, w, h])


            cv2.rectangle(copy, (x, y), (x+w, y+h), (0, 0, 255), 3)

            show_picture("blanck", blanck, 0, "")


            crop = img[y-5:y+h+5, x-5:x+w+5]
            show_picture("crop", crop, 0, "")

            cv2.imwrite("crop" + str(save) + ".png", crop)

            save += 1


    show_picture("copy", copy, 0, "")

















##    #bas
##    l_b1 = np.array([0, 0, 0])
##    u_b1 = np.array([97, 255, 255])
##    mask1 = cv2.inRange(hsv, l_b1, u_b1)
##    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##
##    show_picture("mask1", mask1, 0, "")













