import cv2
import os

import numpy as np


from pictures_function import open_picture
from pictures_function import show_picture
from pictures_function import blanck_picture


liste = os.listdir()

for i in liste:
    if i[:4] == "crop":
        
        img = open_picture(i)
        img = cv2.resize(img, (100, 100))
        show_picture("img", img, 0, "")
    
