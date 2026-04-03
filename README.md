# 🎯 AI-Based Face Recognition Attendance System

## 📌 Overview
This project is an AI-powered attendance system that uses face recognition to automatically mark attendance in real-time.

It detects faces using a CNN-based model and records attendance with subject, date, and time while preventing duplicate entries.

---

## 🚀 Features
- Real-time face detection and recognition
- Subject-wise attendance tracking
- Automatic timestamp logging
- Duplicate prevention (per subject per day)
- Unknown face detection

---

## 🧠 Technologies Used
- Python
- OpenCV
- face_recognition (CNN-based model)
- NumPy
- CSV (for storage)

---

## ⚙️ How It Works
1. Collect face data using `collect_data.py`
2. Encode faces using `encode_faces.py`
3. Run `recognize.py`
4. Enter subject name
5. System detects face and marks attendance

---

## 📂 Project Structure
```
face_attendance_project/
│
├── collect_data.py
├── encode_faces.py
├── recognize.py
├── fix_dlib.py
├── encodings.pickle
├── attendance.csv
├── requirements.txt
└── .gitignore
```

## ⚠️ Note
Dataset is not included due to privacy reasons. Users can create their own dataset using `collect_data.py`.

---

## 🧑‍💻 Author
Khushi Raj
