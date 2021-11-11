import cv2  # unošenje potrebnih knjižnica
import pygame
import os

pygame.init()  # inicijalizacija pygame-a
pygame.mixer.init()

# win=pygame.display.set_mode((1920,1080),pygame.RESIZABLE)#izgled prozora
# pygame.display.set_caption('Super Mario Opening')
# učitavanje podataka
path=os.getcwd()
cust_path=path+'\Custom\Opening.mp3'
orig_path=path+'\Resursi\Zvučni efekti\Opening.wav'

try:
    pygame.mixer.music.load(cust_path)

except:
    pygame.mixer.music.load(orig_path)

pygame.mixer.music.play()

if (cv2.VideoCapture('Custom\Opening.mp4').isOpened()) == True:
    x = 'Custom\Opening.mp4'
else:
    x = 'Resursi\Opening.mp4'

cap = cv2.VideoCapture(x)

while (cap.isOpened()):  # puštanje videozapisa

    ret, frame = cap.read()

    if ret == True:  # zaustavljanje
        cv2.imshow('Super Mario Opening', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            pygame.mixer.music.pause()
            break
    else:
        break

cap.release()  # zatvaranje prozora
cv2.destroyAllWindows()
