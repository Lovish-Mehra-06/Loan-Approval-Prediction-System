# Loan Approval Prediction System

## 🧠 Project Overview

This project builds a machine learning pipeline to predict loan approval using applicant financial and demographic data. It includes data preprocessing, feature engineering, model training, and evaluation using multiple ML algorithms.

## 📌 Problem Statement

Develop an end-to-end machine learning system to predict whether a loan application will be approved based on applicant demographics, financial details, and credit history.

---

## 📊 Dataset

- **Source:** Kaggle Loan Prediction Dataset
- **Type:** Supervised Learning (Classification)
- **Target Variable:** `loan_status` (Y → Approved, N → Not Approved)
- Dataset Shape: (rows, columns)
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

1. **Data Understanding & EDA** – analyzed feature distributions and relationships
2. **Data Cleaning** – handled missing values and inconsistent entries
3. **Feature Engineering** – created `total_income` for better representation
4. **Data Preprocessing** – encoded categorical variables and prepared dataset
5. **Model Building** – trained multiple models:
    - Logistic Regression (baseline)
    - Random Forest
    - XGBoost

6. **Model Evaluation** – compared models using performance metrics
7. **Model Selection** – selected best-performing model

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

> Final results and comparison will be updated after training and tuning.

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
```

---

## 🚀 Future Improvements

- Hyperparameter tuning for improved performance
- Deploy interactive Streamlit web app
- Add model explainability (feature importance, SHAP)
- Improve feature engineering techniques

---

## 💡 Key Insight

Credit history is one of the most influential features in determining loan approval, significantly impacting model predictions.

---

## 👨‍💻 Author

Lovish Mehra
