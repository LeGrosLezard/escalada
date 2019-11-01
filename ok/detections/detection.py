import csv
import cv2
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

from essais_train import *

#Path pictures
from PATHS import path_climbing_holds_originals as p_holds_original


#Picture functions
from pictures_function import picture_colors
from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture







def reshape_thresh(thresh):
    thresh = cv2.resize(thresh, (100, 100))
    return thresh


def to_list(thresh):

    data = []
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):

            if thresh[i, j] > 120:
                nb = 1
            else:
                nb = 0
        
            data.append(nb)

    return data



original_list = os.listdir(p_holds_original)

pp = "../pictures/climbing_holds_r/"

okok = os.listdir(pp)


for i in okok:

    picture = str(pp) + str(i)
    img = open_picture(picture)
    img = cv2.resize(img, (100, 100))

    show_picture("image", img, 0, "")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #_, thresh = cv2.threshold(gray, 0, 255, 0)

    _, thresh = cv2.threshold(gray, 140, 255, 0)
    show_picture("thresh", thresh, 0, "")


    model = joblib.load("test")
    predicting = prediction(thresh, model)
    print(predicting)


























    
