# 📊 Heart Disease Prediction Classification Project

## 📑 Introduction & Background
Cardiovascular diseases (CVDs) remain the leading cause of mortality globally, accounting for millions of deaths annually. Early and accurate detection of heart conditions is critical for effective clinical intervention. This project leverages Machine Learning to analyze key biomedical features and physiological indicators, establishing an automated decision-support system that assists healthcare professionals in early screening and risk assessment.

## 📊 Dataset Specifications

The predictive model is trained on a comprehensive heart disease dataset containing **918 patient observations** with **12 clinical attributes**. Below is the detailed layout of the dataset features:

| Feature Name | Data Type | Description | Valid Values / Units |
| :--- | :--- | :--- | :--- |
| **Age** | Numerical | Age of the patient | Years |
| **Sex** | Categorical | Gender of the patient | M (Male), F (Female) |
| **ChestPainType** | Categorical | Type of chest pain experienced | TA (Typical Angina), ATA (Atypical Angina), NAP (Non-Anginal Pain), ASY (Asymptomatic) |
| **RestingBP** | Numerical | Resting blood pressure level | mm Hg |
| **Cholesterol** | Numerical | Serum cholesterol level | mg/dl |
| **FastingBS** | Categorical | Fasting blood sugar screening | 1 (If FastingBS > 120 mg/dl), 0 (Otherwise) |
| **RestingECG** | Categorical | Resting electrocardiogram results | Normal, ST (ST-T wave abnormality), LVH (Left Ventricular Hypertrophy) |
| **MaxHR** | Numerical | Maximum heart rate achieved | Beats per minute (60 - 202) |
| **ExerciseAngina**| Categorical | Exercise-induced angina | Y (Yes), N (No) |
| **Oldpeak** | Numerical | ST depression induced by exercise relative to rest | Numeric value |
| **ST_Slope** | Categorical | The slope of the peak exercise ST segment | Up (Upsloping), Flat, Down (Downsloping) |
| **HeartDisease** | Target (Binary)| Diagnostic output risk class | 1 (Presence of Heart Disease), 0 (Normal) |

## 💻 Web Application Features
The system is deployed as an interactive clinical web application using the **Streamlit** framework. 
* **User-Centric UI:** Allows users or medical practitioners to input patient metrics via intuitive sliders and dropdown menus.
* **Real-time Pipeline Processing:** Raw inputs are seamlessly transformed using pre-trained `StandardScaler` and `LabelEncoder` objects before evaluation.
* **Instant Risk Probability:** Explores the underlying Random Forest probabilities to output a definitive diagnostic prediction along with a visual health alert status (Red for Alert, Green for Normal).

---

## 📌 Project Overview
This project focuses on predicting the likelihood of heart disease in patients using automated clinical metrics. By analyzing key health indicators, we implemented a complete Machine Learning pipeline and deployed a live, interactive web application for real-time predictions.

🎯 **Live Web Application: https://ml-project-tfnfjrbs2eifrx9qwt5rcn.streamlit.app/ 

---

## 📺 Video Demonstration
The Demo:

---

## 📂 Repository Structure
```text
├── heart.csv                   # Original Dataset
├── heart_disease_model.pkl     # Trained Random Forest Model
├── scaler.pkl                  # Saved StandardScaler
├── *_encoder.pkl               # Saved LabelEncoders for categorical features
├── Final_Project.ipynb         # Jupyter Notebook (EDA, Training & Tuning)
├── app.py                      # Streamlit Application Source Code
├── requirements.txt            # Production Dependencies
└── README.md                   # Project Documentation

```

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
