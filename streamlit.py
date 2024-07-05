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


class_names = ['indian market', 'onion', 'potato', 'tomato'] #1
# class_names = ['indian market','tomato' , 'potato', 'onion']
def load_and_prep_image(image):
    """
    Loads and prepares an image for prediction.
    """
    img = Image.open(image)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    return img_array

st.title('Image Classification with MobileNetV2')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = load_and_prep_image(uploaded_file)
    st.image(image.squeeze(), caption='Uploaded Image', use_column_width=True)
    prediction = model.predict(image)
    class_indices = prediction.argmax(axis=1)
    st.write(f'Prediction: {class_names[class_indices[0]]}')

