from __future__ import print_function
import numpy as np
import tensorflow as tf
import imutils
import cv2
import os

def predict(path):
    # import the necessary packages
    X = []
    model = tf.keras.models.load_model('all_angle.h5')
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cap = cv2.VideoCapture(path)
    fgbg = cv2.createBackgroundSubtractorKNN()
    firstFrame = None
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is not None:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame_copy = frame.copy()
            fgmask = fgbg.apply(frame_copy)
            ret, thresh = cv2.threshold(fgmask,235,255,cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cimg = np.zeros_like(thresh)
            for i in range(len(contours)):
                cv2.drawContours(cimg, contours, i, color=255, thickness=-1)
            cimg = cv2.cvtColor(cimg,cv2.COLOR_GRAY2RGB)
            cimg = cv2.resize(cimg,(240,240))
            cimg = cimg.reshape(-1,240,240,3)
            X.append(cimg)
        else:
            break
        k = cv2.waitKey(50) & 0xff
        if k == 27:
            break
    print("Video Read")
    cap.release()
    print(len(X))
    prediction = []
    for i in X:
        prediction.append(model.predict(i))
    return prediction

if __name__ == '__main__':
    # ls = predict('D:/MINOR_PROJECT/Gait Recognition/gui/001-bg-01-000.avi')
    model = tf.keras.models.load_model('all_angle.h5')
    img = cv2.imread('gei\\000-bg-01-054-12.jpg')
    cv2.imshow('sub',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = img.reshape(1,240,240,3)
    print(model.predict(img))