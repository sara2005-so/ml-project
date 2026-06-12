```markdown
# 📊 Heart Disease Prediction Classification Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-Live-red.svg" alt="Streamlit App">
  <img src="https://img.shields.io/badge/Machine_Learning-Random_Forest-green.svg" alt="Model">
</p>

---

## 📌 Project Overview
This project focuses on predicting the likelihood of heart disease in patients using automated clinical metrics. By analyzing key health indicators, we implemented a complete Machine Learning pipeline and deployed a live, interactive web application for real-time predictions.

🎯 **Live Web Application:** [Click Here to Access the App](https://ml-project-tfnfjrbs2eifrx9qwt5rcn.streamlit.app/)

---

## 📺 Video Demonstration
The Demo: (https://img.shields.io/badge/YouTube-Video_Demo-red?style=for-the-badge&logo=youtube)

## 📂 Repository Structure
```text
├── heart.csv                   # Original Dataset
├── heart_disease_model.pkl     # Trained Random Forest Model
├── scaler.pkl                  # Saved StandardScaler
├── *_encoder.pkl               # Saved LabelEncoders for categorical features
├── Final_Project.ipynb             # Jupyter Notebook (EDA, Training & Tuning)
├── app.py                          # Streamlit Application Source Code
├── requirements.txt                # Production Dependencies
└── README.md                       # Project Documentation

```

---

## 🛠️ Machine Learning Pipeline

### 1. Data Exploration (EDA) & Cleaning

* Investigated **6 key variables** using both univariate and bivariate analysis.
* Included **5 different kinds of plots** (Histograms, Box plots, Correlation Heatmaps, etc.) to detect distributions and outliers.
* Handled non-logical missing values (zeros in Cholesterol and Blood Pressure) by replacing them with the **Median**.

### 2. Feature Engineering & Selection

* **Feature Engineering:** Created a new feature `BP_Category` to classify blood pressure stages.
* **Feature Selection:** Applied **Filter Methods** using correlation matrices to select the top 11 most significant features.

### 3. Model Training & Parameter Tuning

We attempted **3 different algorithms** and compared their performance:

* Logistic Regression
* Support Vector Machine (SVM)
* **Random Forest Classifier** *(Best Performing Model)*

> **Parameter Tuning:** Implemented `GridSearchCV` on the Random Forest model to tune hyperparameters, optimizing the model against overfitting and boosting precision.

---

## 📊 Evaluation & Validation Results

### Model Performance

Validation was highly prioritized to ensure reliability on unseen data. The final Random Forest model achieved evaluation metrics (Precision & Recall) significantly exceeding the 0.3 project threshold.

| Metric | Score | Status |
| --- | --- | --- |
| **Precision** | > 0.80 | ✅ Passed |
| **Recall** | > 0.80 | ✅ Passed |
| **Validation Threshold** | 0.30 | 🚀 Exceeded |

---

## 💻 Tech Stack & Libraries

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, Joblib
* **Deployment:** Streamlit Community Cloud

---

## 👥 Collaborators & Acknowledgments
* Developed with care as part of the final Biotechnology Informatics project.
* Special thanks to the evaluation team and my academic colleagues.
