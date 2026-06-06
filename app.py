import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('best_heart_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Heart Disease Prediction App 🏥")
st.write("Enter patient data to predict heart disease risk.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[("Male", 1), ("Female", 0)], format_func=lambda x: x[0])[1]
resting_bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
max_hr = st.number_input("Max Heart Rate", min_value=50, max_value=220, value=150)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[("No", 0), ("Yes", 1)], format_func=lambda x: x[0])[1]

age_bp_risk = age * resting_bp

if st.button("Predict"):
    input_data = np.array([[age, sex, resting_bp, cholesterol, fasting_bs, max_hr, age_bp_risk, 0, 0, 0]])
    
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    
    if prediction[0] == 1:
        st.error("High Risk of Heart Disease!")
    else:
        st.success("Low Risk of Heart Disease.")