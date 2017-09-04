import cv2
import numpy as np
import _pickle
import glob

import descriptors

comped_imgs = {}
dataStore = "C:/Users/ian/Desktop/PyCV/PyCV/Resources/data/HistClassData"
imgs = ["C:/Users/ian/Desktop/PyCV/PyCV/Resources/pictures/Corgi","C:/Users/ian/Desktop/PyCV/PyCV/Resources/pictures/HotAirBalloon"]

desc = descriptors.RGBHist([8, 8, 8])


for tset in imgs:
    for imgPath in glob.glob(tset + "/*.jpg"):
        imgPath = imgPath.replace('\\','/')
        key = imgPath[imgPath.rfind("/",0,imgPath.rfind("/"))+1:]
        image = cv2.imread(imgPath)
        features = desc.describe(image)
        comped_imgs[key] = features

f = open(dataStore, "wb")
f.write(_pickle.dumps(comped_imgs))
f.close()
