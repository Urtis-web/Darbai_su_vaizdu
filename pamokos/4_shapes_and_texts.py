import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#print(img)
#img[200:300,100:300] = 255,0,0

cv2.line(img,(0,0),(300,300),(75 ,158,200),3)     # linija
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)    # keturkampis  cv2.FILLED ==> vietoje 2 (tam kad uzpildyti visa staciakampi)
cv2.circle(img,(400,50),30,(255,255,0),5)         # apskritimas
cv2.putText(img,"OPENCV",(300,150),cv2.FONT_HERSHEY_TRIPLEX,1,(0,150,0),1) # tekstas



cv2.imshow("Image",img)

cv2.waitKey(0)