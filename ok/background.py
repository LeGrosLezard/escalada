import os
import cv2

import imutils
import numpy as np
import time
import matplotlib.pyplot as plt
from PIL import Image

import cv2
import numpy as np
from matplotlib import pyplot as plt


def open_picture(image, mode):
    """We open picture"""
    if mode == 1:
        img = cv2.imread(image)
    elif mode == 0:
        img = cv2.imread(image, 0)
    return img

def show_picture(name, image, mode, destroy):
    """Show picture"""
    
    cv2.imshow(name, image)
    cv2.waitKey(mode)
    if mode == 1:
        time.sleep(0.000000000000001)
        #cv2.destroyAllWindows()
    if destroy == "y":
        cv2.destroyAllWindows()

def save_picture(name, picture):
    """saving picture"""
    cv2.imwrite(name, picture)

def blanck_picture(img):
    """ Create a black picture"""
    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:, 0:] = 0, 0, 0
    return blank_image


def adjust_gamma(image, gamma):
    """We add light to the video, we play with gamma"""

    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)


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


    for key, value in dico.items():
        if value > max_value and key != (0):
            max_value = value; color = key;


    return dico, color



def rotation(img, degrees):
    """
        Rotation of the picture via his center
    """
    
    rows = img.shape[0]
    cols = img.shape[1]

    img_center = (cols / 2, rows / 2)
    M = cv2.getRotationMatrix2D(img_center, degrees, 1)

    #Rotate picture with white border
    rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(0,0,0))
    #show_picture("rotated", rotated, 0, "y")

    return rotated








def background(img, width, height):

    MM = cv2.ADAPTIVE_THRESH_MEAN_C
    MG = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    T = cv2.THRESH_BINARY

    R = cv2.RETR_TREE
    P = cv2.CHAIN_APPROX_NONE


 
##
##    height, width, channel = img.shape
##    add_w = width % 10
##    add_h = height % 10
##
##    img = cv2.resize(img, (300, 300))
##    height, width, channel = img.shape

    #show_picture("img", img, 0, "")

    
    copy = img.copy()
    ccopy = img.copy()
    ccopsy = img.copy()
    yaya = img.copy()
    cocopy = img.copy()

    dzadazda= img.copy()

    aaaadsytrytr= img.copy()

    

    image_rgb = img
    
    rectangle = (20, 20,width-35, height-35)




    mask = np.zeros(image_rgb.shape[:2], np.uint8)




    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)


    cv2.grabCut(image_rgb, # Our image
                mask, # The Mask
                rectangle, # Our rectangle
                bgdModel, # Temporary array for background
                fgdModel, # Temporary array for background
                10, # Number of iterations
                cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

    # Create mask where sure and likely backgrounds set to 0, otherwise 1
    mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')


    image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]





    return image_rgb_nobg












