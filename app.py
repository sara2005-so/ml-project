import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# 📌 Automatically determine the current directory path for deployment stability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(file_name):
    return os.path.join(BASE_DIR, file_name)

# 1. Load the trained model and transformers using relative paths
model = joblib.load(get_path('heart_disease_model.pkl'))
scaler = joblib.load(get_path('scaler.pkl'))

sex_encoder = joblib.load(get_path('Sex_encoder.pkl'))
chest_pain_encoder = joblib.load(get_path('ChestPainType_encoder.pkl'))
resting_ecg_encoder = joblib.load(get_path('RestingECG_encoder.pkl'))
exercise_angina_encoder = joblib.load(get_path('ExerciseAngina_encoder.pkl'))
st_slope_encoder = joblib.load(get_path('ST_Slope_encoder.pkl'))
bp_category_encoder = joblib.load(get_path('BP_Category_encoder.pkl'))

# 2. Streamlit app interface configuration
st.set_page_config(page_title="Heart Disease Prediction App", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter the patient's clinical metrics below to predict the likelihood of heart disease.")

st.sidebar.header("Patient Input Features")

# 3. Input elements
age = st.sidebar.slider("Age", 1, 100, 50)
sex = st.sidebar.selectbox("Sex", ["M", "F"])
chest_pain = st.sidebar.selectbox("Chest Pain Type (ChestPainType)", ["ATA", "NAP", "ASY", "TA"])
resting_bp = st.sidebar.number_input("Resting Blood Pressure (RestingBP in mm Hg)", min_value=50, max_value=250, value=120)
cholesterol = st.sidebar.number_input("Serum Cholesterol (Cholesterol in mg/dl)", min_value=50, max_value=600, value=200)
fasting_bs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl (FastingBS)", [0, 1])
resting_ecg = st.sidebar.selectbox("Resting Electrocardiogram (RestingECG)", ["Normal", "ST", "LVH"])
max_hr = st.sidebar.slider("Maximum Heart Rate Achieved (MaxHR)", 60, 250, 150)
exercise_angina = st.sidebar.selectbox("Exercise-Induced Angina (ExerciseAngina)", ["N", "Y"])
oldpeak = st.sidebar.number_input("ST Depression Induced by Exercise (Oldpeak)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
st_slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment (ST_Slope)", ["Up", "Flat", "Down"])

# 4. Feature Engineering: Blood Pressure Categorization
def categorize_bp(bp):
    if bp < 120: return 'Normal'
    elif 120 <= bp < 140: return 'Prehypertension'
    else: return 'Hypertension'

bp_category = categorize_bp(resting_bp)

# 5. Prediction button logic
if st.button("Analyze & Predict"):
    try:
        # Encode categorical inputs using loaded transformers
        sex_encoded = sex_encoder.transform([sex])[0]
        chest_pain_encoded = chest_pain_encoder.transform([chest_pain])[0]
        resting_ecg_encoded = resting_ecg_encoder.transform([resting_ecg])[0]
        exercise_angina_encoded = exercise_angina_encoder.transform([exercise_angina])[0]
        st_slope_encoded = st_slope_encoder.transform([st_slope])[0]
        bp_category_encoded = bp_category_encoder.transform([bp_category])[0]
        
        # Combine all features into a dictionary structure
        all_features_dict = {
            'Age': age, 'Sex': sex_encoded, 'ChestPainType': chest_pain_encoded,
            'RestingBP': resting_bp, 'Cholesterol': cholesterol, 'FastingBS': fasting_bs,
            'RestingECG': resting_ecg_encoded, 'MaxHR': max_hr, 'ExerciseAngina': exercise_angina_encoded,
            'Oldpeak': oldpeak, 'ST_Slope': st_slope_encoded, 'BP_Category': bp_category_encoded
        }
        
        # Create a DataFrame for safe alignment
        input_df = pd.DataFrame([all_features_dict])
        
        # Match features dynamically to the exact order used during model training
        model_features = model.feature_names_in_
        final_input_df = input_df[model_features]
        final_features = final_input_df.values
        
        # Perform inference
        prediction = model.predict(final_features)[0]
        prediction_proba = model.predict_proba(final_features)[0][1]
        
        # 6. Render localized analytical outputs
        st.subheader("Diagnostic Analysis Results:")
        if prediction == 1:
            st.error(f"⚠️ Warning: The patient has a high probability of heart disease ({prediction_proba*100:.1f}%).")
        else:
            st.success(f"🎉 Result: Patient metrics appear normal/healthy. (Probability of being disease-free: {(1 - prediction_proba)*100:.1f}%).")
            
    except Exception as e:
        st.error(f"An error occurred during processing: {e}")