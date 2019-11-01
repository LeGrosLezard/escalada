#os for operation on files
import os
"""Here we have specials functions for read, show, save
and create a white empty picture"""


#sys for indicate path
import sys
sys.path.append(r"C:\Users\jeanbaptiste\Desktop\assiette\v2\main")

#numpy for transform picture to array
import numpy as np

#cv2 and PIL are library for treatment on pictures
import cv2
from PIL import Image



def open_picture(image):
    """We open picture for read it."""

    img = cv2.imread(image)
    return img


def show_picture(name, image, mode, destroy):
    """We Show the picture

        - mode 1 is for an automatic display,
        - mode 0 wait a press key for destroy picture,
        -destroy y is for remove picture.
    """

    if mode == 0:
        cv2.imshow(name, image)
        cv2.waitKey(mode)

    if mode == 1:
        time.sleep(1)
        cv2.destroyAllWindows()

    if destroy == "y":
        cv2.destroyAllWindows()


def save_picture(name, picture):
    """saving picture we need:

        - his name "".extension,
        - the picture readed.
        
    """

    cv2.imwrite(name, picture)



def blanck_picture(img):
    """ Create a black picture bgr, we need:

        - his dimensions (width and height),
        - his color (0, 0, 0) is blanck default.

    """


    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0

    return blank_image



def main_color_background(img):
    """
        Here we recup the main color
        by the recurrent pixel
    """

    dico = {}; max_value = 0; color = []

    #Convert picture to array
    im = Image.fromarray(img)
    #data from array recup value pixels 
    for value in im.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1

    #recup main pixel presence
        #except for green pixels (use for our contours)
    for key, value in dico.items():
        if value > max_value and key[0] > 50 and key[1] > 50 and key[2] > 50:
            max_value = value; color = key;

    return color



def picture_colors(original_list, p_holds_original, mode_lecture):

    liste = []
    images = []
    last_category = 0
    b=0;g=0;r=0;counter=0;counter_max=0;

    print("Recup Colors...")

    for i in original_list:
        picture = str(p_holds_original) + str(i)
        img = open_picture(picture)
        img = cv2.resize(img, (100, 100))
        
        category = int(i[4:-6])
        if category != last_category:

##            print("Pictures from ", counter_max - counter, \
##                  counter_max, "Have main color:",\
##                  int(b/counter), int(g/counter), int(r/counter))

            liste.append([int(b/counter), int(g/counter), int(r/counter)])
            images.append(counter)

            b=0;g=0;r=0;counter=0;

        else:
            color = main_color_background(img)

            b += color[0]
            g += color[1]
            r += color[2]
            counter+=1

        last_category = category

        if mode_lecture == "0":
            show_picture("image", img, 0, "")
        elif mode_lecture == "1":
            show_picture("image", img, 1, "")
        elif mode_lecture == "2":
            pass
        counter_max += 1


    return liste, images




def take_features(img):

    MM = cv2.ADAPTIVE_THRESH_MEAN_C
    MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    T = cv2.THRESH_BINARY

    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE



    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    th3 = cv2.adaptiveThreshold(gray, 255, MG, T,11,5)
    show_picture("th3", th3, 0, "")




    contours, _ = cv2.findContours(th3, R, P)

    maxi = 0
    maxi1 = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > maxi:
            maxi = cv2.contourArea(cnt)
        if cv2.contourArea(cnt) < maxi and\
           cv2.contourArea(cnt) > maxi1:
            maxi1 = cv2.contourArea(cnt)



    blanck = blanck_picture(img);
    blanck = cv2.cvtColor(blanck, cv2.COLOR_BGR2GRAY)


    for cnts in contours:
        if cv2.contourArea(cnts) == maxi1:
            print(cv2.contourArea(cnts))
            cv2.drawContours(blanck,[cnts],-1,(255,255,255), 1)
            #cv2.fillPoly(blanck, pts =[cnts], color=(255, 255, 255))

            show_picture("blanck", blanck, 0, "")





























