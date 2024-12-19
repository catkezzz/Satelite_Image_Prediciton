import streamlit as st
import eda
import prediction

halaman = st.sidebar.selectbox('Choose a page: ', ('EDA','Prediction'))

if halaman == 'EDA':
    eda.run()
else:
    prediction.run()