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

def csv_write():
    with open('test.csv', 'w') as file:
        writer = csv.writer(file)
        file.write("label;")
        for i in range(0, 10000):
            file.write("pixel"+str(i)+";")

        file.write("\n")


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



def write_data_into_csv(data, label):

    with open('test.csv', 'a') as file:
        writer = csv.writer(file)
        file.write(label+";")
        for i in data:
            file.write(str(i)+";")

        file.write("\n")






def csv_to_list():
    """
        Recup data from csv
        we only take dataframe[1:]
            because dataframe[1] is the label
        we add data on list
            X for 0 or 1 pix of picture
            Y for label
    """

    file =  open("test.csv", 'r')

    #dataframe[1] == label !
    dataframe = file.readlines()
    dataframe = dataframe[1:]

    X = []; Y = [];

    for i in dataframe:

        #it serve to make a list of list it's a work list
        liste_w = []

        for j in i:
            #if element is a jump add
                #work list to final list and
                #reinitialize it
            if j == "\n":
                X.append(liste_w)
                liste_w = []

            else:
                #pass if it's a delemiter or " "
                if j == ";" or j == " ":
                    pass

                else:
                    #If we put a str(label)
                    try:
                        j = int(j)
                        liste_w.append(int(j))
                    except:
                        liste_w.append(str(j))

    #Here we recup label
    for i in X:
        Y.append(i[0])
        del i[0]

    return X, Y



def training(X, Y, model_name):
    """
        We define train data and test data
        We call SVC who's linear function
        We define model name
        And make the prediction
    """

    #define test and train data
    X_train, Y_train =  X, Y
    X_test,Y_test = X, Y

    #call SVC function
    model = svm.SVC(kernel="linear",C=2)
    #model = KNeighborsClassifier(n_neighbors=3)
    #fit method


    model.fit(X_train,Y_train)

    #create model
    joblib.dump(model, model_name)

    #predict it!
    predictions = model.predict(X_test)

    print("Score", metrics.accuracy_score(Y_test, predictions))




def reshape_thresh(thresh):
    thresh = cv2.resize(thresh, (100, 100))
    return thresh

def prediction(thresh, model):
    """Call prediction with last operation
    of reshape and flatted"""

    thresh = reshape_thresh(thresh)
    rows, cols = thresh.shape

    X = to_list(thresh)

    predictions = model.predict([X])
    

    return predictions[0]









