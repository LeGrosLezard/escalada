import os
import cv2
import csv
import joblib
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import metrics
from skimage import feature
from skimage import exposure
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

import os
import cv2
import time

#Path pictures
from PATHS import path_climbing_holds_originals as p_holds_original

#Picture functions
from pictures_function import picture_colors
from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture


from essais_train import *

def picture_colors(original_list, p_holds_original, mode_lecture):

    label = 0
    last_category = 0

    liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a",
             "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v"]





    csv_write()


    for i in original_list:
        #open
        picture = str(p_holds_original) + str(i)
        img = open_picture(picture)
        img = cv2.resize(img, (100, 100))

        #label
        category = int(i[4:-6])
        print(category)
        if category != last_category:
            label += 1
            liste[label]
        else:
            label = label
            liste[label]

        last_category = category


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, 0)
        thresh = reshape_thresh(thresh)

        data = to_list(thresh)
        print(data)

        write_data_into_csv(data, liste[label])




##        #display
##        if mode_lecture == "0":
##            show_picture("image", img, 0, "")
##        elif mode_lecture == "1":
##            show_picture("image", img, 1, "")
##        elif mode_lecture == "2":
##            pass


        print(liste[label])






















#oInput = input("  See with not automatic = 0 \n See with automatic pass = 1\n No see = 2")

oInput= ""
original_list = os.listdir(p_holds_original)



picture_colors(original_list, p_holds_original, oInput)






















