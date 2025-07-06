import streamlit as st
import cv2
from PIL import Image
from ultralytics import YOLO
import numpy as np
import matplotlib.pyplot as plt

# Load the trained YOLO model
model = YOLO("fruit_detection_model.pt")
# Streamlit UI setup
st.title("Fruit Detection with YOLOv8")

# Image uploader UI
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# Function to load image and convert to appropriate format
def load_image(image_file):
    img = Image.open(image_file)
    return img

if uploaded_file is not None:
    # Load the image from the file uploader
    image = load_image(uploaded_file)

    # Convert to OpenCV format (RGB to BGR)
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Use Streamlit spinner to show loading message while detection is running
    with st.spinner("Performing object detection..."):
        # Perform object detection with YOLOv8
        results = model(img_bgr)

    # Get the predicted image (annotated image)
    annotated_img = results[0].plot() if isinstance(results, list) else results.plot()

    # Convert back to RGB for display in Streamlit
    annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

    # Display images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.header("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.header("Detection Result")
        st.image(annotated_img_rgb, use_container_width=True)

    # Success message once detection is complete
    st.success("Object detection completed!")