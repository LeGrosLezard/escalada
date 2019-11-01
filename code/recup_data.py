import os

#Path pictures
from PATHS import path_climbing_holds_originals as p_holds_original

#Picture functions
from pictures_function import picture_colors



oInput = input("  See with not automatic = 0 \n See with automatic pass = 1\n No see = 2")


original_list = os.listdir(p_holds_original)
colors, _, = picture_colors(original_list, p_holds_original, oInput)
print(colors, _)


