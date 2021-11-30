#!/usr/bin/env python3
import numpy
import pygame
import cv2
W = 1920//2
H = 1080//2
pygame.init()
screen = pygame.display.set_mode((W, H))



def process_frame(img):
    
    img = cv2.resize(img, (W,H))
    surf = pygame.surfarray.make_surface(img)     
    surf_center = (
        (W-surf.get_width())/2,

        (H-surf.get_height())/2
    )
    surface = pygame.Surface((50, 50))

    

    print(surf) 
    surf = pygame.transform.rotate(surf, 90)
    screen.blit(surf, surf_center)
    pygame.display.update() 
    print(img.shape)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test_nyc.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
