import cv2 #unošenje potrebnih knjižnica
import numpy as np
import pygame as pg

pg.init() #inicijalizacija pygame-a
pg.mixer.init()

win=pg.display.set_mode((1920,1080),pg.RESIZABLE)#izgled prozora
pg.display.set_caption('Super Mario Opening')
#učitavanje podataka
try:
  pg.mixer.music.load('Custom\Opening.mp3')

except:
    pg.mixer.music.load('Resursi\Zvučni efekti\Opening.mp3')

pg.mixer.music.play()

if (cv2.VideoCapture('Custom\Opening.mp4').isOpened())==True:
  x='Custom\Opening.mp4'
else:
  x='Resursi\Opening.mp4'

cap=cv2.VideoCapture(x)

while(cap.isOpened()):#puštanje videozapisa

  ret, frame = cap.read()

  if ret == True: #zaustavljanje
    cv2.imshow('Super Mario Opening',frame)
    if cv2.waitKey(22) & 0xFF == ord('q'):
      pg.mixer.music.pause()
      break
  else: 
    break

cap.release() #zatvaranje prozora
cv2.destroyAllWindows()
