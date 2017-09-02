import cv2
import numpy as np


def single_color(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    upper_b = np.array([64, 177, 231],np.uint8)
    lower_b = np.array([37, 33, 114],np.uint8)
    mask = cv2.inRange(img, lower_b, upper_b)
    return mask

def blur_average(img,size=5):
    kernel = np.ones((size,size),np.float32)/(size*size)
    avg = cv2.filter2D(img,-1,kernel)
    return avg

def remove_noise(img, size=9):
    return cv2.bilateralFilter(img,size,75,75)

def test(img):
    #kernel = np.matrix([[0,1,0],
    #                    [1,-4,1],
    #                    [0,1,0]])
    kernel = np.matrix([[0,0,1,0,0],
                        [0,0,1,0,0],
                        [1,1,-8,1,1],
                        [0,0,1,0,0],
                        [0,0,1,0,0]])
    avg = cv2.filter2D(img,-1,kernel)
    return avg