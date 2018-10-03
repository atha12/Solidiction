from PIL import Image
import pytesseract
import cv2
import os
import imutils
import datetime
from datetime import date
import re

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,help="img4.jpg")
# args = vars(ap.parse_args())

# print(type(args["image"]))

image = cv2.imread("img4.jpg")
# image = imutils.resize(image,1024,665)
# image = image[200:440,290:660]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

gray = cv2.medianBlur(gray, 3)
 
# make a check to see if median blurring should be done to remove
# noise
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
# print(text)


match = re.search(r'\d{2}\/\d{2}\/\d{4}', text)
date = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()
print(date)


 
# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)