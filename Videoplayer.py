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
  if y==1:
    pg.mixer.music.load('Resursi\Zvučni efekti\Opening.mp3')
  else:
    pg.mixer.music.load('Resursi\Zvučni efekti\Opening2.mp3')
pg.mixer.music.play()

if (cv2.VideoCapture('Custom\Opening.mp4').isOpened())==True:
  x='Custom\Opening.mp4'

cap=cv2.VideoCapture(x)
x=cap.get(cv2.CAP_PROP_FPS)

while(cap.isOpened()):#puštanje videozapisa

  ret, frame = cap.read()

  if ret == True: #zaustavljanje
    cv2.imshow('Super Mario Opening',frame)
    if cv2.waitKey(int(round((1/x)*1000,0))-12) & 0xFF == ord('q'):
      pg.mixer.music.pause()
      break
  else: 
    break

cap.release() #zatvaranje prozora
cv2.destroyAllWindows()
