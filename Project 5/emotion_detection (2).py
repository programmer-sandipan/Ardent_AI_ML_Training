# ==========================================
# Real-Time Emotion Detection (No DeepFace)
# ==========================================

import cv2
import numpy as np
from keras.models import load_model

# Load face detection model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load emotion model
emotion_model = load_model("emotion_model.hdf5", compile=False)

# Emotion labels
emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Sad",
    "Surprise",
    "Neutral"
]

# Start webcam (Mac compatible)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (64, 64))
        roi_gray = roi_gray / 255.0
        roi_gray = np.reshape(roi_gray, (1, 64, 64, 1))

        prediction = emotion_model.predict(roi_gray)
        max_index = int(np.argmax(prediction))
        emotion = emotion_labels[max_index]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, emotion, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (0,255,0), 2)

    cv2.imshow("Emotion Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()