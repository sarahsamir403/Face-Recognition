import streamlit as st
import cv2
import numpy as np

st.title('Face Recognition Application')

uploaded_file = st.file_uploader("Choose an image...", type= ['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    img = np.array(bytearray(uploaded_file.read()), dtype = np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    st.image(img, caption = 'Uploaded Image', use_column_width = True, channels = 'BGR')

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #st.image(gray_img, caption = 'Gray Image', use_column_width = True, channels = 'GRAY')

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 240,0), 2)
    st.image(img, channels = 'BGR', caption = 'Face Detected')
