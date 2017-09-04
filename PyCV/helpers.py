import cv2
import numpy as np

def take_pic(camera):
    retval, img = camera.read()
    return img

def load_colortest():
    return cv2.imread('E:\Folders\OpenCV\Resources\colortest.jpg')

def save_pic(img):
    cv2.imwrite('E:\Folders\OpenCV\Resources\img.png',img)

def disp_pic(img, resize=False, wait=True):
    if resize:
        cv2.imshow('test',cv2.resize(img,(500,500)))
    else:
        cv2.imshow('test',img)
    if wait:
        cv2.waitKey(0)

def set_hd(camera):
    camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

def hist_curve(im):
    h = np.zeros((300,256,3))
    if len(im.shape) == 2:
        color = [(255,255,255)]
    elif im.shape[2] == 3:
        color = [ (255,0,0),(0,255,0),(0,0,255) ]
    for ch, col in enumerate(color):
        hist_item = cv2.calcHist([im],[ch],None,[256],[0,256])
        cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
        hist=np.int32(np.around(hist_item))
        pts = np.int32(np.column_stack((np.arange(256).reshape(256,1),hist)))
        cv2.polylines(h,[pts],False,col)
    y=np.flipud(h)
    return y