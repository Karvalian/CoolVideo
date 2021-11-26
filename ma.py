#!/usr/bin/env python3
import numpy

import cv2
yep = input("Enter the filename of your vod: ")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
def process_frame(img):
    img = cv2.resize(img, (1920//2, 1080//2))
    cv2.imshow('image', img)
    cv2.waitKey(1)
    print(img.shape)



if __name__ == "__main__":
    cap = cv2.VideoCapture(yep)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
