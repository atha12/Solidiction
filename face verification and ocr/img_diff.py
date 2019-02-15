import cv2
import numpy as np


def get_faces(f_cascade, colored_img, scaleFactor=1.1):
    #just making a copy of image passed, so that passed image is not changed 
    img_copy = colored_img.copy()

    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)

    return faces


def get_face(f_cascade, colored_img, scaleFactor=1.1):
    faces = get_faces(f_cascade, colored_img)

    (x, y, w, h) = faces[0]
    crop_img = colored_img[y:y+h, x:x+w]

    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)

    return crop_img


#load another image 
test1 = cv2.imread('img4.jpg')

#load cascade classifier training file for haarcascade 
haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#call our function to detect faces 
face_detected_img = get_face(haar_face_cascade, test1)


video_capture = cv2.VideoCapture(0)

face = None

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    faces = get_faces(haar_face_cascade, frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    if (key & 0xFF == ord(' ')) and len(faces) == 1:
        x, y, w, h = faces[0]
        face = frame[y:y+h, x:x+w]
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

# img1 = cv2.imread("banana1.jpg")
# img2 = cv2.imread("banana3.jpg")

img1 = face
img2 = face_detected_img

shape = (min(img1.shape[0], img2.shape[0]), min(img1.shape[1], img2.shape[1]))

# img1.resize(size, Image.ANTIALIAS)
# img2.resize(size, Image.ANTIALIAS)

img1 = cv2.resize(img1, shape, interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2, shape, interpolation=cv2.INTER_AREA)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.waitKey(0)

difference = cv2.subtract(img1, img2)

acc = sum(sum(difference == [0])) / (shape[0]*shape[1])

print(acc)

# result = not np.any(difference)

# if result is True:
#     print "The images are the same"
# else:
#     cv2.imwrite("result.jpg", difference)
# print "the images are different"
