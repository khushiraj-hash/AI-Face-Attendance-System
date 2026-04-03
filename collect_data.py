import sys
import dlib
sys.modules['dlib'] = dlib

import face_recognition
import cv2
import os

# take name
name = input("Enter your name: ")

# create folder
path = 'dataset/' + name
os.makedirs(path, exist_ok=True)

# start camera
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert BGR → RGB (VERY IMPORTANT)
    rgb_frame = frame[:, :, ::-1]

    # detect faces using CNN
    faces = face_recognition.face_locations(rgb_frame)

    for (top, right, bottom, left) in faces:
        count += 1

        # crop face (COLOR, not grayscale)
        face = frame[top:bottom, left:right]

        # save image
        cv2.imwrite(f"{path}/{name}_{count}.jpg", face)

        # draw rectangle
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow('Collecting Images', frame)

    # stop after 30 images or ESC
    if cv2.waitKey(1) == 27 or count >= 30:
        break

cap.release()
cv2.destroyAllWindows()

print("✅ Dataset collected successfully!")