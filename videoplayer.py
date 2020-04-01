import cv2
import numpy as np
import pygame as pg
pg.mixer.init()
pg.mixer.music.load('Resursi\Zvučni efekti\Opening.mp3')
pg.mixer.music.play()
win=pg.display.set_mode((1920,1080),pg.RESIZABLE)
a=pg.image.load('Resursi\mario ikona.png')  #ikona
pg.display.set_icon(a)
cap = cv2.VideoCapture('Resursi\Super Mario Opening.mp4')
pg.mixer.music.play()
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



