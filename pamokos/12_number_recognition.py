import cv2
########################################################
nplateCascade = cv2.CascadeClassifier(r'C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu/haarcascade_russian_plate_number.xml')
minArea = 200
color = (255,0,255)
########################################################
cap = cv2. VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nplateCascade.detectMultiScale(imgGray, 1.1, 10)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]     #reegin of interest
            cv2.imshow("ROI",imgRoi)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break