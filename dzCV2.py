import cv2
import numpy as np


photo = np.zeros((600, 1200, 3), dtype='uint8')

for i in range(100):
    cv2.rectangle(photo, (i, i), (photo.shape[1]-i, photo.shape[0]-i), (0, 0, 0), thickness=cv2.FILLED)


cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 80, (255, 255, 255), 2)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(40, 40), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.ellipse(img=photo, center=(photo.shape[1]//2, photo.shape[0]//2), axes=(20, 20), angle=0., startAngle=0, endAngle=180, color=(0,255,0),thickness=3)
cv2.line(photo, (560, 270), (560, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (580, 270), (580, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (620, 270), (620, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (640, 270), (640, 300), (255, 0, 0), thickness=3)
cv2.line(photo, (560, 270), (580, 270), (0, 0, 255), thickness=3)
cv2.line(photo, (620, 270), (640, 270), (0, 0, 255), thickness=3)
cv2.rectangle(photo, (50, 20), (100, 100), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (150, 40), (100, 100), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (250, 120), (100, 100), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (900, 800), (1100, 200), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (1000, 800), (250, 100), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (1050, 500), (100, 100), (128, 0, 128), thickness=3)
cv2.rectangle(photo, (1150, 50), (100, 100), (128, 0, 128), thickness=3)
cv2.imshow('kjjjjj', photo)
cv2.waitKey(0)