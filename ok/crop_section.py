import cv2
import os
from PIL import Image
import numpy as np


from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture
from background import background


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
        if value > max_value and key[0] > 50 and key[1] > 50 and key[2] > 50 and\
           key[0] < 200 and key[1] < 200 and key[2] < 200:
            max_value = value; color = key;

    return color, dico












liste = os.listdir()


MM = cv2.ADAPTIVE_THRESH_MEAN_C
MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
T = cv2.THRESH_BINARY

R = cv2.RETR_TREE
P = cv2.CHAIN_APPROX_NONE




        
for i in liste:
    if i[:4] == "crop" and i != "crop_section.py":

        print(i)
        
        img = open_picture(i)
        img = cv2.resize(img, (100, 100))
        show_picture("img", img, 0, "")


        height, width, channel = img.shape

        img = background(img, width, height)


        color, dico = main_color_background(img)
        print(color)




        show_picture("img", img, 0, "")












        
