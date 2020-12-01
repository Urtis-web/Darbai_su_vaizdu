import cv2
import os


image_path = r'C:\Users\Urtis\PycharmProjects\Darbai_su_vaizdu\cat.jpg'
if (os.path.exists(image_path) == True):
    image = cv2.imread(image_path)
    cv2.imshow("windows", image)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('tiltas_copy.png',image)
        cv2.destroyAllWindows()
else:
    print("File " + image_path + " doesnt exist!")

