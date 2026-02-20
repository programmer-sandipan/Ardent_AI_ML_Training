# Face Detection Project using OpenCV
# OpenCV = Open Source Computer Vision Library


import cv2


# Load Pre-trained Haar Cascade Model

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# Start Webcam

cap = cv2.VideoCapture(2, cv2.CAP_AVFOUNDATION)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to quit")
print("Press 's' to save image")



# Main Loop

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display face count
    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Show output window
    cv2.imshow("Face Detection System", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save image
    if key == ord('s'):
        cv2.imwrite("captured_face.jpg", frame)
        print("Image saved successfully!")

    # Press 'q' to exit
    if key == ord('q'):
        break


# Release Resources

cap.release()
cv2.destroyAllWindows()