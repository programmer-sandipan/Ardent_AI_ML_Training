
[README.md](https://github.com/user-attachments/files/25434537/README.md)
# 🎯 Face Detection System

A real-time face detection application built with Python and OpenCV, using Haar Cascade classifiers to detect and highlight faces through a webcam feed.

---

## 📸 Demo

The system draws a green bounding box around every detected face in real time, along with a live face count overlay on the screen.
<img width="652" height="447" alt="image" src="https://github.com/user-attachments/assets/455e2667-1a09-498e-bb30-061ac148261d" />


## 🚀 Features

- Real-time face detection via webcam
- Live face count overlay on video feed
- Capture and save snapshots with a single keypress
- Lightweight and fast using Haar Cascade classification
- Clean visual feedback with green bounding boxes

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| OpenCV (`cv2`) | Computer vision & webcam I/O |
| Haar Cascade XML | Pre-trained face detection model |

---

## 📋 Prerequisites

- Python 3.7 or higher
- A connected webcam

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/face-detection-system.git
   cd face-detection-system
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install opencv-python
   ```

---

## ▶️ Usage

Run the script from the terminal:

```bash
python face_detection.py
```

### Keyboard Controls

| Key | Action |
|-----|--------|
| `S` | Save current frame as `captured_face.jpg` |
| `Q` | Quit the application |

---

## 🔧 Configuration

You can tune the detection parameters inside the script to adjust accuracy and performance:

```python
face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,    # How much the image is scaled down at each step (higher = faster, less accurate)
    minNeighbors=5      # How many neighbors each candidate rectangle needs (higher = fewer false positives)
)
```

### Webcam Index

If your webcam isn't detected, change the device index:

```python
cap = cv2.VideoCapture(0)   # Try 0, 1, or 2 depending on your system
```

> **macOS users:** The script uses `cv2.CAP_AVFOUNDATION` as the backend, which is the recommended capture API for macOS.

---

## 📁 Project Structure

```
face-detection-system/
│
├── face_detection.py       # Main application script
├── captured_face.jpg       # Saved snapshots (generated at runtime)
└── README.md               # Project documentation
```

---

## 🧠 How It Works

1. **Load Model** — OpenCV's built-in `haarcascade_frontalface_default.xml` is loaded as the face classifier.
2. **Capture Frames** — The webcam streams frames in real time using `VideoCapture`.
3. **Grayscale Conversion** — Each frame is converted to grayscale to improve detection speed and accuracy.
4. **Face Detection** — The Haar Cascade classifier scans the frame for face-like patterns using `detectMultiScale`.
5. **Draw & Display** — Green rectangles are drawn around detected faces, and the total count is rendered on screen.

---

## 🐛 Troubleshooting

**Webcam not opening?**
- Ensure no other application is using the webcam.
- Try changing the `VideoCapture` index to `0` or `1`.
- On macOS, make sure the terminal or IDE has camera permissions.

**Too many false positives?**
- Increase `minNeighbors` (e.g., `7` or `10`).

**Missing faces being detected?**
- Decrease `scaleFactor` closer to `1.1` for a more thorough scan.
- Ensure good, even lighting on your face.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [OpenCV](https://opencv.org/) — Open Source Computer Vision Library
- [Viola-Jones Algorithm](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework) — The foundation of Haar Cascade detection
