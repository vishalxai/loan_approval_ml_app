import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("../model/xgb_model.pkl")

# Title
st.title("🏦 Loan Approval Prediction App")
st.markdown("Predict whether a loan will be approved based on applicant details.")

# User input form
st.header("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", ["1.0", "0.0"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Preprocess inputs
def preprocess_input():
    data = {
        "Gender": 1 if gender == "Male" else 0,
        "Married": 1 if married == "Yes" else 0,
        "Education": 1 if education == "Graduate" else 0,
        "Self_Employed": 1 if self_employed == "Yes" else 0,
        "Dependents": int(dependents.replace("3+", "3")),
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_amount_term,
        "Credit_History": float(credit_history),
        "Property_Area_Semiurban": 1 if property_area == "Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area == "Urban" else 0,
    }

    df = pd.DataFrame([data])
    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]
    df["Log_TotalIncome"] = np.log1p(df["TotalIncome"])

    # Ensure column order matches training data
    ordered_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 
                    'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'TotalIncome', 
                    'Log_TotalIncome', 'Property_Area_Semiurban', 'Property_Area_Urban']
    
    return df[ordered_cols]


# Prediction
if st.button("Predict"):
    input_df = preprocess_input()
    prediction = model.predict(input_df)[0]
    
    # ✅ Save input + prediction to CSV log
    import os
    log_file = "prediction_log.csv"
    log_data = input_df.copy()
    log_data["Prediction"] = prediction

    if not os.path.exists(log_file):
        log_data.to_csv(log_file, index=False)
    else:
        log_data.to_csv(log_file, mode='a', header=False, index=False)

    # ✅ Display result
    if prediction == 1:
        st.success("✅ Loan is likely to be **Approved**!")
    else:
        st.error("❌ Loan is likely to be **Rejected**.")