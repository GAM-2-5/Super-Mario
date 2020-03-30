import cv2
import numpy as np
import pygame as pg
pg.mixer.init()
pg.mixer.music.load('Opening.mp3')
pg.mixer.music.play()
win=pg.display.set_mode((960,540),pg.RESIZABLE)
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Super Mario Opening.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-fram
  ret, frame = cap.read()
  if ret == True:
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    # Press Q on keyboard to  exit

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else: 
    break
# When everything done, release the video capture object
cap.release()
# Closes all the frames
#cv2.destroyAllWindows()


