import cv2
import matplotlib.pyplot as plt


def showImage():
    fileName = "../images/lena.jpg"
    img = cv2.imread(fileName, cv2.IMREAD_COLOR)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(imgRGB)
    plt.show()

showImage()