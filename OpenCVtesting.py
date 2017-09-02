import cv2
import numpy as np
from matplotlib import pyplot as plt

import disp_video
import img_operations as imop
import helpers

camera = cv2.VideoCapture(0)
helpers.set_hd(camera)



camera.release()
cv2.destroyAllWindows()
