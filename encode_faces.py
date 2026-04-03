import os
import cv2
import sys
import dlib
sys.modules['dlib'] = dlib
import face_recognition
import pickle
import fix_dlib

dataset_path = "dataset"

known_encodings = []
known_names = []

# loop through dataset
for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect face locations
        face_locations = face_recognition.face_locations(rgb)

        if len(face_locations) == 0:
            continue

        # 👉 IMPORTANT CHANGE (this fixes error)
        encodings = face_recognition.face_encodings(rgb, known_face_locations=face_locations, num_jitters=1)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person)

# save encodings

data = {"encodings": known_encodings, "names": known_names}

with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("✅ Encoding complete!")