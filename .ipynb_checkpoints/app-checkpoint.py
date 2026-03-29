import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🎗️ Breast Cancer Prediction App")
st.write("Enter tumor measurements to predict if it's Malignant or Benign")

# Input sliders
clump = st.slider("Clump Thickness", 1, 10, 5)
cell_size = st.slider("Uniformity of Cell Size", 1, 10, 1)
cell_shape = st.slider("Uniformity of Cell Shape", 1, 10, 1)
adhesion = st.slider("Marginal Adhesion", 1, 10, 1)
epithelial = st.slider("Single Epithelial Cell Size", 1, 10, 2)
nuclei = st.slider("Bare Nuclei", 1, 10, 1)
chromatin = st.slider("Bland Chromatin", 1, 10, 3)
nucleoli = st.slider("Normal Nucleoli", 1, 10, 1)
mitoses = st.slider("Mitoses", 1, 10, 1)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([{
        'Clump Thickness': clump,
        'Uniformity of Cell Size': cell_size,
        'Uniformity of Cell Shape': cell_shape,
        'Marginal Adhesion': adhesion,
        'Single Epithelial Cell Size': epithelial,
        'Bare Nuclei': nuclei,
        'Bland Chromatin': chromatin,
        'Normal Nucleoli': nucleoli,
        'Mitoses': mitoses
    }])
    
    scaled_data = pd.DataFrame(scaler.transform(input_data), 
                                columns=input_data.columns)
    prediction = model.predict(scaled_data)
    
    if prediction[0] == 2:
        st.success("✅ Benign — No Cancer Detected!")
    else:
        st.error("⚠️ Malignant — Cancer Detected!")