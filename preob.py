import cv2
import numpy as np

image = cv2.imread('color_text.jpg')
black = np.zeros_like(image, dtype='uint8')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ed = cv2.Canny(blur, 30, 30)

contours, _ = cv2.findContours(ed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

upper_contours = []
middle_contours = []
lower_contours = []

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    if y < image.shape[0] / 4.8:
        upper_contours.append(contour)

    elif y < 2 * image.shape[0] / 4.8:
        middle_contours.append(contour)

    else:
        lower_contours.append(contour)

cv2.drawContours(black, upper_contours, -1, (0, 255, 0), 1)
cv2.drawContours(black, middle_contours, -1, (0, 0, 255), 1)
cv2.drawContours(black, lower_contours, -1, (255, 0, 255), 1)


cv2.imshow('result', black)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('res', image)
cv2.waitKey(0)