# ❤️ Heart Disease Prediction Project

An end-to-end Machine Learning project designed to predict the likelihood of heart disease and deployed as an interactive, production-ready web application.

## 🚀 Live Web App
Experience the live interactive application here: [Insert Your Streamlit App Link Here](https://your-app-url.streamlit.app)

---

## 📌 Project Pipeline

### 1. Exploratory Data Analysis (EDA)
- Analyzed dataset characteristics using over 5 distinct visualization types across 6 core medical variables.
- Investigated feature distributions, correlations, and successfully identified statistical outliers.

### 2. Data Cleaning & Preprocessing
- Addressed clinical anomalies (such as irrational zero values in Cholesterol and RestingBP) by imputing them with the feature **Median**.
- Encoded categorical variables into numerical formats using `LabelEncoder`.
- Normalized numerical features via `StandardScaler` to optimize distance-based algorithm performance.

### 3. Feature Engineering & Selection
- **Feature Engineering:** Developed a domain-specific feature (`BP_Category`) to classify blood pressure into clinical sub-types.
- **Feature Selection:** Implemented a **Filter Method** based on a Pearson correlation matrix to isolate and select the top 11 most predictive features.

### 4. Model Training & Hyperparameter Tuning
- Evaluated 3 distinct classification algorithms: Logistic Regression, Support Vector Machines (SVM), and Random Forest.
- Performed rigorous hyperparameter optimization via `GridSearchCV` using 5-Fold Cross-Validation, specifically optimizing for **Recall** to minimize critical false negatives.

### 5. Validation & Evaluation
- Utilized an 80/20 Train/Test split protocol to ensure strict validation principles and safeguard the model against **Overfitting**.
- The finalized Random Forest model achieved robust classification metrics (Precision, Recall, and F1-Score) comfortably exceeding project benchmarks.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Data & ML Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, Joblib
- **Deployment & UI:** Streamlit Cloud

---

## 📁 Repository Structure
- `heart.csv` - The raw clinical dataset.
- `Final_Project.ipynb` - Jupyter Notebook containing complete EDA, preprocessing, and model training workflows.
- `app.py` - Core Streamlit web application source code.
- `*.pkl` - Serialized artifacts including the final trained model, scaler, and categorical encoders.
