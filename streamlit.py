import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf

# Load the saved model
model = load_model(r"D:\ninja_cart_cv\notebooks\final_model_ninja.h5")
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

