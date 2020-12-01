import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\cat.jpg')
print(img.shape)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
#  cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)