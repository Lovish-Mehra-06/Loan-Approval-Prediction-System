# Loan Approval Prediction System

## 🛠 Status

![Status](https://img.shields.io/badge/Project-In%20Progress-yellow)

## 🧠 Project Overview

This project builds a machine learning pipeline to predict loan approval using applicant financial and demographic data. It includes data preprocessing, feature engineering, model training, and evaluation using multiple ML algorithms.

## 📌 Problem Statement

Develop an end-to-end machine learning system to predict whether a loan application will be approved based on applicant demographics, financial details, and credit history.

---

## 📊 Dataset

- **Source:** Kaggle Loan Prediction Dataset
- **Type:** Supervised Learning (Classification)
- **Target Variable:** `loan_status` (Y → Approved, N → Not Approved)
- Dataset Shape: (614, 13)
- Total Features: 13

---

## ⚙️ Tech Stack

- Programming: **Python**
- Data Handling: **Pandas, Numpy**
- Visualization: **Matplotlib, Seaborn**
- Machine Learning: **Scikit-learn, XGBoost**
- Model Persistence: **Joblib**
- Deployment: **Streamlit**
- Development Environment: **Jupyter Notebook**

---

## 🔍 Project Workflow

1. Data Loading & Inspection
2. Missing Value Analysis
3. Exploratory Data Analysis (EDA)
4. Feature Engineering (Total Income, etc.)
5. Encoding categorical variables
6. Train-test split
7. Baseline models (Logistic Regression, RF, XGBoost)
8. Hyperparameter tuning (RandomizedSearchCV)
9. Model comparison using F1-score
10. Final model selection

---

## 📈 Model Performance

**Models Evaluated:**

- Logistic Regression
- Random Forest
- XGBoost

**Evaluation Metrics:**

- Accuracy
- Precision
- Recall
- F1-score

## 🏆 Best Model

- Model: XGBoost (after tuning)
- Evaluation Metric: F1-score
- Final Accuracy: 78% (f1-score: 85%)

## 📊 Evaluation Details

- Confusion Matrix used for performance analysis
- Focused on F1-score due to class imbalance

---

## 📁 Project Structure

```
Loan-Prediction/
│
├── data/          # Raw dataset
├── notebook/      # EDA and experimentation
├── model/         # Saved model files
├── app.py         # Streamlit deployment
├── README.md
├── requirements.txt
├── .gitignore
```

## 🚀 How to Run

### 1️⃣ Clone the repository

```markdown id="allin1"
git clone https://github.com/Lovish-Mehra-06/Loan-Approval-Prediction-System.git
cd "Loan Approval Prediction System"
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Jupyter Notebook (EDA + Model Training)

```bash
jupyter notebook
```

### 4️⃣ Run Streamlit App (Deployment)

```bash
streamlit run app.py
```

### Note:

- Ensure `model/loan_approval_prediction_model.pkl` exists
- Ensure `model/features.pkl` exists

---

## 🚀 Improvements Implemented

- Hyperparameter tuning using RandomizedSearchCV for better model performance
- Built multiple models (Logistic Regression, Random Forest, XGBoost) and compared results
- Engineered features like Total Income for improved prediction accuracy
- Encoded categorical variables for model compatibility
- Saved final trained model and feature schema for deployment

## 📌 Possible Extensions

- Add model explainability using SHAP or feature importance plots
- Deploy full Streamlit web application (in prog)
- Improve UI/UX of prediction interface

---

## 💡 Key Insight

- Credit history and total income are the most influential features in predicting loan approval.
- Tree-based models captured nonlinear relationships better than linear models, but required tuning to avoid overfitting.

---

## 👨‍💻 Author

Lovish Mehra
