import streamlit as st
from PIL import Image

def run():
    # Membuat Title
    st.title('Satelite Imagery Prediction')
        #Menambah Deskripsi
    st.write('Made by **Catherine Kezia Wijaya**')
    st.write('Source: https://www.kaggle.com/datasets/mahmoudreda55/satellite-image-classification')

    st.markdown('---')

    # Menambahkan Gambar
    image = Image.open('satelite-imagery.webp')
    st.image(image, caption='Satelite Imagery')

    # Membuat garis lurus horizontal
    st.markdown('---')

    st.write('## **Description**')
    st.write('''Remote sensing is a technology that has recently become important for various applications, such as mapping, environmental monitoring, disaster mitigation,
    and more. Advances in this field and the improved quality of satellite images
    (as well as their easy accessibility) have driven the need for automatic
    interpretation of these images.    
    The RSI-CB256 dataset contains images from various sensors and 
    snapshots from Google Maps, covering four classes that reflect
    the diversity of landscapes and objects on Earth:''')
    st.write('''    
    - Clouds
    - Deserts
    - Green Areas
    - Water Bodies
             
    This dataset is crucial for supporting the development of classification
    models capable of automatically categorizing satellite images with high
    accuracy.''')          


    st.write('## **Objective**')
    st.write('The objectives of this project are:')
    st.write('''
    - To develop a deep learning model capable of classifying satellite images into four classes based on the RSI-CB256 dataset.
    - To evaluate the model's performance using accuracy and F1 score metrics, as well as optimize the model to achieve good generalization on new data.
    - To contribute to the advancement of deep learning algorithms in satellite image interpretation.
    - To apply the model in real-world scenarios, such as land mapping, change detection, area monitoring, and more.
''')

    st.markdown('---')

    st.write('## **Image Types**')
    st.write('This section is to show previews of the 4 types of satelite images that are recognizable by this model prediction')

    st.write('### Cloudy')
    st.image(Image.open('cloudy.png'), caption='Satelite Imagery')

    st.write('### Desert')
    st.image(Image.open('desert.png'), caption='Satelite Imagery')

    st.write('### Green Area')
    st.image(Image.open('green_area.png'), caption='Satelite Imagery')

    st.write('### Water Bodies')
    st.image(Image.open('green_area.png'), caption='Satelite Imagery')

