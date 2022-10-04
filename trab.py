# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:53:30 2022

@author: sergi
"""
import numpy as np
import cv2 as cv

def limiarizacao(img, t: int, acima: bool, brilho: int):
    if acima:
        x = img >= t
    else:
        x = img < t

    img = img.astype(int)

    if brilho < 0:
        img[x] = np.maximum(img[x]+brilho, 0)
    else:
        img[x] = np.minimum(img[x]+brilho, 255)

    # agora damos cast de volta pra uint8
    img = img.astype(np.uint8)

    cv.imshow("teste", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1)


limiarizacao(cv.imread("coelho.jpg",cv.IMREAD_GRAYSCALE), 200, False, -255)