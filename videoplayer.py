import cv2
import numpy as np
import pygame as pg
pg.mixer.init()
pg.mixer.music.load('Opening.mp3')
pg.mixer.music.play()
win=pg.display.set_mode((1920,1080),pg.RESIZABLE)

cap = cv2.VideoCapture('Super Mario Opening.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while(cap.isOpened()):

  ret, frame = cap.read()
  if ret == True:

    cv2.imshow('Super Mario Opening',frame)


    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  else: 
    break

cap.release()



