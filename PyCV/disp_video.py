import cv2
import numpy as np

def nothing(x):
    pass

def disp_sliders_hsv(camera):
    cv2.namedWindow('img')
    cv2.createTrackbar('HMAX','img',0,179,nothing)
    cv2.createTrackbar('HMIN','img',0,179,nothing)
    cv2.createTrackbar('SMAX','img',0,255,nothing)
    cv2.createTrackbar('SMIN','img',0,255,nothing)
    cv2.createTrackbar('VMAX','img',0,255,nothing)
    cv2.createTrackbar('VMIN','img',0,255,nothing)
    cv2.createTrackbar('SAVE','img',0,1,nothing)

    cv2.setTrackbarPos('HMAX','img',255)
    cv2.setTrackbarPos('SMAX','img',255)
    cv2.setTrackbarPos('VMAX','img',255)

    while True:
        retval, img = camera.read()
        HMax = cv2.getTrackbarPos('HMAX','img')
        HMin = cv2.getTrackbarPos('HMIN','img')
        SMax = cv2.getTrackbarPos('SMAX','img')
        SMin = cv2.getTrackbarPos('SMIN','img')
        VMax = cv2.getTrackbarPos('VMAX','img')
        VMin = cv2.getTrackbarPos('VMIN','img')

        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        if cv2.getTrackbarPos('SAVE','img') == 0:
            upper_b = np.array([HMax, SMax, VMax],np.uint8)
            lower_b = np.array([HMin, SMin, VMin],np.uint8)
        else:
            upper_b = np.array([64, 177, 231],np.uint8)
            lower_b = np.array([37, 33, 114],np.uint8)

        mask = cv2.inRange(imghsv, lower_b, upper_b)
        img = cv2.bitwise_and(img, img, mask=mask)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        cv2.imshow('img',img)

def disp_custom(img_op_func, camera):
    while True:
        retval, img = camera.read()

        img = img_op_func(img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        cv2.imshow('img',img)


if __name__ == "__main__" :
    camera = cv2.VideoCapture(0)

    disp_sliders_hsv(camera)

    camera.release()