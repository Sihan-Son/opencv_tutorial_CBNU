import cv2
import numpy as np


def showImage():
    fileName = "../images/lena.jpg"
    img = cv2.imread(fileName, cv2.IMREAD_COLOR)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()
