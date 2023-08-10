import os
import cv2
import numpy as np

filter = np.array([[1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]])

rootpath='./'
img = cv2.imread(os.path.join(rootpath, "cameraman.png"))
print(type(img), img.shape, img.dtype)
# print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(gray_img)
print(type(gray_img), gray_img.shape, gray_img.dtype)