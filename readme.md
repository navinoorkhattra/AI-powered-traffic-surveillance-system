## Overview
An AI-powered traffic surveillance system using **WOA** & **ACO** for efficient monitoring. Utilizes **YOLOv8** for detection and **DeepSORT** for tracking.

## Prerequisites 🛠️
- **Python 3.12.1** → [Download](https://www.python.org/downloads/)

## Setup 🏗️
1. Install dependencies:
   ```sh
   pip install numpy opencv-python tensorflow torch torchvision ultralytics scikit-learn deep_sort_realtime flask textblob language-tool-python
   ```
2. Clone repository:
   ```sh
   git clone https://github.com/your-username/ai-traffic-surveillance.git && cd ai-traffic-surveillance
   ```
3. Update pip if needed:
   ```sh
   py -m ensurepip --default-pip && py -m pip install --upgrade pip setuptools wheel
   ```
4. Test the camera:
   ```sh
   python test_camera.py
   ```

## Run 🚀
Start the Flask app:
```sh
python app.py
```
Access via `http://127.0.0.1:5000`.

## Optimization 🧠
- **WOA**: Optimizes detection cost.
- **ACO**: Improves traffic flow predictions.

## Deployment ⚡
Convert YOLO model to **TFLite**:
```sh
yolo export model=yolov8n.pt format=tflite
```