import streamlit as st
import pickle
import numpy as np 
from PIL import Image

def run():
    with open('best_cnn_model.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    st.title('Satelite Image Prediction')
    uploaded_file = st.file_uploader("Choose an Image (Only for cloudy, desert, green area, and water bodies image)", type=["jpg", "png", "jpeg, webp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width=True)
        image = image.resize((64, 64))
        x = np.array(image) / 255.0 
        

        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        y_pred_proba = model.predict(images)
        y_pred_class = np.argmax(y_pred_proba[0])
        class_name = list(['Cloudy', 'Desert', 'Green area', 'Water'])
        y_pred_class_name = class_name[y_pred_class]

        st.write('## Prediction : {}'.format(y_pred_class_name))

