#Python librairies
import os
import cv2
import numpy as np

#Path pictures
from PATHS import path_wall as p_wall
from PATHS import path_climbing_holds_r as p_holds
from PATHS import path_climbing_holds_originals as p_holds_original

#Picture functions
from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture
from pictures_function import take_features



def features():
    pass






def main_recognition():


    #Create list of folder contains
    original_list = os.listdir(p_holds_original)

    for i in original_list:
        print("category :", i[4:-6], "name:", i)

        picture = str(p_holds_original) + str(i)

        img = open_picture(picture)
        img = cv2.resize(img, (100, 100))

        take_features(img)

        show_picture("image", img, 0, "")





main_recognition()









































