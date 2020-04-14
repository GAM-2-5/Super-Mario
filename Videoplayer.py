import cv2
import numpy as np
import pygame as pg
import random

for i in range (1):
    y=random.randint(1,2)

pg.init()
pg.mixer.init()
a=pg.image.load('Resursi\mario ikona.png')
pg.display.set_icon(a)
win=pg.display.set_mode((1920,1080),pg.RESIZABLE)
pg.display.set_caption('Super Mario Opening')

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

else:
  if y==1:
    x='Resursi\Opening.mp4'
  else:
    x='Resursi\Opening2.mp4'

cap=cv2.VideoCapture(x)
x=cap.get(cv2.CAP_PROP_FPS)

while(cap.isOpened()):

  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Super Mario Opening',frame)
    if cv2.waitKey(int(round((1/x)*1000,0))-12) & 0xFF == ord('q'):
      pg.mixer.music.pause()
      break
  else: 
    break

cap.release()
cv2.destroyAllWindows()
