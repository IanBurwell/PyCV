import cv2
import numpy as np
import helpers

camera = cv2.VideoCapture(0)
helpers.set_hd(camera)

grabbed, frame = camera.read()
h, w, c = frame.shape

while cv2.waitKey(10) != ord("n"):
    grabbed, frame = camera.read()
    if not grabbed:
        break

    h, w, c = frame.shape
    frame = cv2.rectangle(frame,(w/2+100,h/2+100),(w/2-100,h/2-100),(0,255,0),3)
    frame = cv2.flip(frame,1)
    cv2.imshow('hist',helpers.hist_curve(frame[h/2-100:h/2+100, w/2-100:w/2+100]))
    cv2.imshow("img", frame)

#setup ROI
track_window = (w/2-100,h/2-100,200,200)
roi = frame[h/2-100:h/2+100, w/2-100:w/2+100]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
roi_hist = cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256])
cv2.normalize(roi_hist, roi_hist, 0, 240, cv2.NORM_MINMAX)

terminationCriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while True:
    grabbed, frame = camera.read()
    if not grabbed:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #backProj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    backProj = cv2.calcBackProject([hsv], [0,1 ], roi_hist, [0, 180, 0, 256], 1)

    r, track_window = cv2.CamShift(backProj, track_window, terminationCriteria)
    pts = cv2.boxPoints(r)
    pts = np.int64(pts)
    cv2.polylines(frame, [pts], True, (0,0,255), 2)

    frame = cv2.flip(frame,1)

    cv2.imshow("img", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
