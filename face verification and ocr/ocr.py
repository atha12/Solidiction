from PIL import Image
import pytesseract
import cv2
import os
import imutils
import datetime
from datetime import date
import re



image = cv2.imread("img4.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

gray = cv2.medianBlur(gray, 3)

text = pytesseract.image_to_string(gray)


match = re.search(r'\d{2}\/\d{2}\/\d{4}', text)
date = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()
print(date)

