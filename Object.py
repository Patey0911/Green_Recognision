import cv2
import numpy as np

def nothing(x):
    pass

img=cv2.VideoCapture(0)
#cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H", "Trackbars",0, 255,nothing)
cv2.createTrackbar("L-S", "Trackbars",0, 255,nothing)
cv2.createTrackbar("L-V", "Trackbars",0, 255,nothing)
cv2.createTrackbar("U-H", "Trackbars",0, 255,nothing)
cv2.createTrackbar("U-S", "Trackbars",0, 255,nothing)
cv2.createTrackbar("U-V", "Trackbars",0, 255,nothing)


while(True):
    _, frame=img.read()

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L-H", "Trackbars")
    l_s=cv2.getTrackbarPos("L-S", "Trackbars")
    l_v=cv2.getTrackbarPos("L-V", "Trackbars")
    u_h=cv2.getTrackbarPos("U-H", "Trackbars")
    u_s=cv2.getTrackbarPos("U-S", "Trackbars")
    u_v=cv2.getTrackbarPos("U-V", "Trackbars")


    lower_green=np.array([26,176,75])
    upper_green=np.array([73,255,255])
    mask=cv2.inRange(hsv, lower_green, upper_green)

    result=cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("result",result)
    #cv2.imshow("mask",mask)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

img.release()
cv2.destroyAllWindows()