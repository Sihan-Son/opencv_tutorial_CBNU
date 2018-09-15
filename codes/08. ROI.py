import cv2

src = cv2.imread('../images/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI('imgae', src)
print("ROI = ", roi)

x, y, w, h = roi[0], roi[1], roi[2], roi[3]
img = src[y: y+h, x:x+h]

cv2.imshow("ROI", img)
cv2.waitKey()
cv2.destroyAllWindows()

