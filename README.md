# 🏥 Heart Disease Risk Prediction App

[![Streamlit App](https://static.streamlit.io/badge-gradient-gradient.svg)](YOUR_STREAMLIT_APP_LINK_HERE)

An End-to-End Machine Learning project designed to predict heart disease risk using patient clinical data. This project includes a complete pipeline from data processing to a live web application deployment.

---

## 🚀 Live Demo
Experience the application here: 
👉 **[Heart Disease Prediction App](YOUR_STREAMLIT_APP_LINK_HERE)**

---

## 📌 Project Features
The model analyzes 10 specific clinical features to determine risk levels:

* **Patient Profile:** Age and Sex.[cite: 1]
* **Clinical Metrics:** Resting Blood Pressure, Cholesterol, and Maximum Heart Rate.[cite: 1]
* **Diagnostic Tests:** Fasting Blood Sugar (> 120 mg/dl).[cite: 1]
* **Feature Engineering:** Includes an `Age-BP Risk` factor (Age × Resting Blood Pressure) to capture combined cardiovascular stress.[cite: 1]

---

## 🛠️ Technical Workflow
1. **Preprocessing:** Data is normalized using a `StandardScaler` to ensure prediction accuracy.[cite: 1]
2. **Model:** A pre-trained Machine Learning model (`best_heart_model.pkl`) is used for classification.[cite: 1]
3. **Deployment:** Built with **Streamlit** for an interactive, user-friendly interface.[cite: 1]

---

## 📊 How to Run Locally

### 1. Clone the project
```bash
git clone [https://github.com/sara2005-so/ml-project.git](https://github.com/sara2005-so/ml-project.git)
cd ml-project
