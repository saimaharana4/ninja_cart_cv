import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path
import os

def find_base_dir():
    """
    Dynamically find the base directory based on the existence of 'notebooks' subdirectory.
    """
    current_dir = Path(os.getcwd())
    while current_dir != current_dir.root:
        if (current_dir / 'notebooks').exists():
            return current_dir
        current_dir = current_dir.parent
    return None  # or raise an error if preferred

base_dir = find_base_dir()
model_path = base_dir / "notebooks" / "final_model_ninja.h5"

model = load_model(model_path)

class_names = ['INDIAN MARKET', 'ONION', 'POTATO', 'TOMATO']

def load_and_prep_image(image):
    """
    Loads and prepares an image for prediction.
    """
    img = Image.open(image)
    img = img.resize((224, 224))  # Resize to the input size expected by the model
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    return img_array

st.title('Vegetable Image Classification')

# Description of the app
st.write("""
This application utilizes a deep learning model to classify images of vegetables. 
Simply upload an image of a vegetable, and the app will predict whether the image is of an onion, potato, tomato, or represents a scene from an Indian market.
""")

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# if uploaded_file is not None:
#     image = load_and_prep_image(uploaded_file)
#     st.image(image.squeeze(), caption='Uploaded Image', use_column_width=True, width=100)  # Reduced width for smaller display
#     prediction = model.predict(image)
#     class_indices = prediction.argmax(axis=1)
#     prediction_text = f'**Prediction: {class_names[class_indices[0]]}**'
#     # Display prediction in a box with some styling
#     st.success(prediction_text)

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# if uploaded_file is not None:
#     image = load_and_prep_image(uploaded_file)
#     # Set a specific size for the image display
#     st.image(image.squeeze(), caption='Uploaded Image', width=200, use_column_width=False)
#     prediction = model.predict(image)
#     class_indices = prediction.argmax(axis=1)
#     prediction_text = f'**Prediction: {class_names[class_indices[0]]}**'
#     # Display prediction in a styled box
#     st.success(prediction_text)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = load_and_prep_image(uploaded_file)
    # Using columns to center the image
    col1, col2, col3 = st.columns([1,2,1])
    with col2:  # This column is the middle column
        st.image(image.squeeze(), caption='Uploaded Image', use_column_width=True)
        prediction = model.predict(image)
        class_indices = prediction.argmax(axis=1)
    st.success(f'**Prediction: {class_names[class_indices[0]]}**')