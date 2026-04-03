import sys
import dlib
sys.modules['dlib'] = dlib

import cv2
import face_recognition
import pickle
import csv
import os
from datetime import datetime

# 🔥 Ask subject
subject = input("Enter subject: ")

# load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

# attendance file
file_name = "attendance.csv"

# create file if not exists
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Subject", "Date", "Time", "Status"])

# function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # check duplicate
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if row[0] == name and row[1] == subject and row[2] == date:
                    return  # already marked

    # add new entry
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, subject, date, time, "Present"])

# start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, face_locations)

    for encoding, (top, right, bottom, left) in zip(encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

            # 🔥 mark attendance
            mark_attendance(name)

        # draw
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()