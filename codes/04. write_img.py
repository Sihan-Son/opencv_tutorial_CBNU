import cv2


def saveImage():
    fileName = "../images/lena.jpg"
    img = cv2.imread(fileName, cv2.IMREAD_COLOR)

    cv2.imwrite("../saves/lena.bmp", img)
    cv2.imwrite("../saves/lena.png", img)
    cv2.imwrite("../saves/lena2.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    cv2.imwrite("../saves/lena.jpg", img, [cv2.IMWRITE_JPEG_LUMA_QUALITY, 90])

saveImage()
