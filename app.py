import streamlit as st
import pandas as pd
import joblib

# Load model + features
model = joblib.load("model/loan_approval_prediction_model.pkl")
features = joblib.load("model/features.pkl")

st.title("🏦 Loan Approval Prediction System")

# ---------------- INPUTS ----------------
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")

loanamount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term")
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])


# ---------------- ENCODING ----------------
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

dependents = 3 if dependents == "3+" else int(dependents)

property_area = {"Urban": 0, "Rural": 1, "Semiurban": 2}[property_area]

# ---------------- FEATURE ENGINEERING ----------------
total_income = applicant_income + coapplicant_income

# ---------------- INPUT DATAFRAME ----------------
input_data = pd.DataFrame(
    [
        [
            gender,
            married,
            dependents,
            education,
            self_employed,
            loanamount,
            loan_amount_term,
            credit_history,
            property_area,
            total_income,
        ]
    ],
    columns=features,
)

# ---------------- PREDICTION ----------------
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Loan Approved")
    else:
        st.error("❌ Loan Rejected")
