#unošenje potrebnih python knjižnica
import cv2
import numpy as np
import pygame as pg
#inicijalizacija pygame-a
pg.init()
pg.mixer.init()
#izgled prozora
a=pg.image.load('Resursi\mario ikona.png')
pg.display.set_icon(a)
win=pg.display.set_mode((1920,1080),pg.RESIZABLE)
pg.display.set_caption('Super Mario Opening')
#zvuk videa
try:
  pg.mixer.music.load('Custom\Opening.mp3')

except: 
  pg.mixer.music.load('Resursi\Zvučni efekti\Opening.mp3')

pg.mixer.music.play()
#otvaranje video file-a
if (cv2.VideoCapture('Custom\Opening.mp4').isOpened())==True:
  x='Custom\Opening.mp4'

else:
  x='Resursi\Opening.mp4'

cap=cv2.VideoCapture(x)
x=cap.get(cv2.CAP_PROP_FPS)
#puštanje svakog frame-a videa određenu količinu vremena do puštanja idućeg
while(cap.isOpened()):

  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Super Mario Opening',frame)
    if cv2.waitKey(int(round((1/x)*1000,0))-12) & 0xFF == ord('q'): #zatvaranje prozora tipkom Q
      pg.mixer.music.pause()
      break
  else: 
    break
#zatvaranje prozora
cap.release()
cv2.destroyAllWindows()
