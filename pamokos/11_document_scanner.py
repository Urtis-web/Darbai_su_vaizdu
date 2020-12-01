import cv2
import numpy as np
##############################################################
widthImg = 480
heightImg = 640
##############################################################
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      # padaro vaizda nespalvota
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)         # sublurinimas
    imgCanny = cv2.Canny(imgBlur,200,200)               # surandami konturu krastai

    kernel = np.ones((5,5))                             # pastorinami konturu krastai
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)  # pastorinami konturu krastai
    imgThres = cv2.erode(imgDial,kernel,iterations=1)   # pastorinami konturu krastai
    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:               # visada parenkama didziausia reiksme
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest                                                # grazina didziausio konturo reiksmes

def reorder(myPoints):                            # tasku surusiavimas eiles tvarka
    myPoints = myPoints.reshape((4, 2))           # nurodomos tasku koordinates tiksliai
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)                         # sudedami 4 tasku koordinaciu skaiciai tarpsavyje

    myPointsNew[0] = myPoints[np.argmin(add)]     # surandama maziausia koordinaciu sumos verte (pirmas taskas)
    myPointsNew[3] = myPoints[np.argmax(add)]     # surandama didziausia koordinaciu sumos verte (ketvirtas taskas)

    diff = np.diff(myPoints,axis=1)               # skirtumas
    myPointsNew[1] = myPoints[np.argmin(diff)]    # (antras taskas)
    myPointsNew[2] = myPoints[np.argmax(diff)]    # (trecias taskas)
    return myPointsNew

def getWarp(img,biggest):

    biggest = reorder(biggest)
    pts1 = np.float32(biggest)                                                          # nurodomi rasti lapo kampu taskai
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]           # Krastu nukropinimas
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))                            # Krastu nukropinimas

    return imgCropped

def stackImages(scale,imgArray): # Nuotrauku suklijavimas
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

while True:
    success, img = cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)

    if biggest.size !=0:                  # jeigu kamera mato lapa
        imgWarped = getWarp(img,biggest)
        imageArray = ([img,imgThres],
                  [imgContour,imgWarped])
    else:                                 # jeigu kamera nemato lapo

        imageArray = ([img, imgThres],
                      [img, img])

    stackedImages = stackImages(0.6,imageArray)

    cv2.imshow("Work Flow", stackedImages)
    if len(biggest) > 0:
        cv2.imshow("Image Warped", imgWarped)
    else:
        cv2.destroyWindow("Image Warped")
    #cv2.imshow("Image Warped", imgWarped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break