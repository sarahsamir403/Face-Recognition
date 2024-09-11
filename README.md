# Face Recognition Application

## Overview

This is a simple face recognition application built using **Streamlit** and **OpenCV**. The application allows users to upload an image, detects faces in the image using a pre-trained Haar Cascade model, and highlights them with bounding boxes.

## Features

- Upload an image in `jpg`, `jpeg`, or `png` format.
- Display the uploaded image.
- Detect faces in the uploaded image using OpenCV's Haar Cascade Classifier.
- Display the image with detected faces highlighted by yellow bounding boxes.

## Requirements

- Python 3.x
- Streamlit
- OpenCV
- NumPy
  
## Installation

1. Clone the repository or download the script.
   
   ```bash
   git clone https://github.com/your-repo/face-recognition-app.git

   pip install streamlit opencv-python-headless numpy
   cd face-recognition-app
   streamlit run face_recognition.py


