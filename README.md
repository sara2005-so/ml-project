# 🏥 Heart Disease Risk Prediction App

[![Streamlit App](https://static.streamlit.io/badge-gradient-gradient.svg)](YOUR_STREAMLIT_APP_LINK_HERE)

An End-to-End Machine Learning project designed to predict whether a patient has a high or low risk of heart disease based on clinical parameters. This repository contains the complete machine learning pipeline, from data preprocessing and feature engineering to deploying the final model as an interactive web application.

---

## 🚀 Live Application
You can test the live interactive app and input patient data here:
👉 **[Open the Live Streamlit App](YOUR_STREAMLIT_APP_LINK_HERE)**

---

## 📌 Project Architecture & Pipeline

The project follows a structured data science workflow to ensure robust and clinical-grade predictions:

1. **Exploratory Data Analysis (EDA):** Analyzed risk factors, distributions, and clinical correlations within the dataset.
2. **Feature Engineering:** Created domain-specific interaction features (e.g., `Age × Resting Blood Pressure Risk Factor`) to capture non-linear relationships that enhance model accuracy.
3. **Data Normalization:** Applied robust feature scaling using `StandardScaler` to ensure all continuous medical metrics are on the same scale before feeding them into the classifier.
4. **Model Deployment:** Exported the trained pipeline (`best_heart_model.pkl` & `scaler.pkl`) and developed a production-ready user interface using **Streamlit**.

---

## 📊 Model Features & Inputs

The Streamlit application takes real-time patient inputs for the following clinical features:

* **Age:** Patient's age (1–120).
* **Sex:** Categorical (Male/Female).
* **Resting Blood Pressure:** Resting blood pressure in mm Hg.
* **Cholesterol:** Serum cholesterol in mg/dl.
* **Fasting Blood Sugar:** Fasting blood sugar > 120 mg/dl (Yes/No).
* **Max Heart Rate:** Maximum heart rate achieved during exercise.
* **Age-BP Risk Factor:** An engineered interaction feature (`Age` × `Resting Blood Pressure`) representing cumulative cardiovascular stress over time.

---

## 🏆 Model Evaluation

Multiple classification models were tested and optimized. Since this is a medical diagnosis task, the evaluation focused heavily on **Recall (Sensitivity)** to ensure that high-risk patients are not missed (minimizing False Negatives).

| Model | Accuracy | Precision | Recall (Sensitivity) | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| **Baseline Classifier** | 0.XX | 0.XX | 0.XX | 0.XX |
| **Optimized Classifier (Final)** | **0.XX** | **0.XX** | **0.XX** | **0.XX** |

*(Note: Please update the `0.XX` placeholders with the exact metrics from your `ml_proj.ipynb` notebook).*

---

## 💻 Local Installation & Setup

To run the application locally on your machine, execute the following commands in your terminal:

### 1. Clone the Repository
```bash
git clone [https://github.com/sara2005-so/ml-project.git](https://github.com/sara2005-so/ml-project.git)
cd ml-project
