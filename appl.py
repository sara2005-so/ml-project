import streamlit as st
import numpy as np
import joblib

# تحميل الموديل والـ scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Heart Disease Prediction App")

st.write("Enter patient information")

Age = st.number_input("Age", min_value=1, max_value=120)

Sex = st.selectbox(
    "Sex",
    [0, 1]
)

ChestPainType = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

RestingBP = st.number_input(
    "Resting Blood Pressure",
    min_value=50,
    max_value=250
)

Cholesterol = st.number_input(
    "Cholesterol",
    min_value=0,
    max_value=700
)

FastingBS = st.selectbox(
    "Fasting Blood Sugar",
    [0, 1]
)

RestingECG = st.selectbox(
    "Resting ECG",
    [0, 1, 2]
)

MaxHR = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250
)

ExerciseAngina = st.selectbox(
    "Exercise Angina",
    [0, 1]
)

Oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0
)

ST_Slope = st.selectbox(
    "ST Slope",
    [0, 1, 2]
)

Age_Group = st.selectbox(
    "Age Group",
    [0, 1, 2]
)

if st.button("Predict"):

    data = np.array([[
        Age,
        Sex,
        ChestPainType,
        RestingBP,
        Cholesterol,
        FastingBS,
        RestingECG,
        MaxHR,
        ExerciseAngina,
        Oldpeak,
        ST_Slope,
        Age_Group
    ]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")