import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("../images/lena.jpg",cv2.IMREAD_GRAYSCALE)

hist1 = cv2.calcHist([src], [0], None, [32], [0, 256])
hist2 = cv2.calcHist([src], [0], None, [256], [0, 256])

#1
hist1 = hist1.flatten()
hist2 = hist2.flatten()

#2
plt.title('hist : binX = np.array(32)')
plt.plot(hist1, color='r')
binX = np.array(range(32))
plt.bar(binX, hist1, width=1,  color='b')
plt.show()

#3
plt.title('hist : binX = np.array(32)*8')
binX = np.array(range(32))*8
plt.plot(binX, hist1, color='r')
plt.bar(binX, hist1, width=8, color='b')
plt.show()

#4
plt.title('hist : binX = np.array(256)')
plt.plot(hist2, color='r')
binX = np.array(range(256))
plt.bar(binX, hist2, width=1,  color='b')
plt.show()