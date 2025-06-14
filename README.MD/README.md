# 🏦 Loan Approval Prediction App

A complete end-to-end **Machine Learning project** that predicts whether a loan application is likely to be approved or rejected, based on applicant details. Built with **Python, Pandas, XGBoost, Streamlit**, and best practices in model deployment and reproducibility.

---

## 🚀 Demo

📍 Streamlit App (_local_)  
📍 GitHub Repo: [Loan Approval GitHub](https://github.com/vishalxai/loan_approval_ml_app)

## 📌 Problem Statement

Loan default risk is one of the major risks for banks. This project aims to assist financial institutions in identifying whether a **loan applicant is eligible** for approval based on multiple demographic and financial features.

---

## 🧠 ML Workflow Summary

| Stage | Description |
|-------|-------------|
| 📂 Data | CSV-based cleaned loan dataset |
| 📊 Preprocessing | One-hot encoding, log transformations |
| 🤖 Model | XGBoost Classifier |
| ✅ Evaluation | Accuracy, Cross-validation |
| 🖥️ Deployment | Streamlit web app |
| 🧾 Logging | CSV log of predictions with inputs |

---

## 📁 Project Structure
Loan_approval_project/
├── app/
│   └── app.py                  ← Streamlit frontend
│   └── prediction_log.csv      ← Auto-logged predictions
├── data/
│   └── loan_data.csv           ← Input dataset
├── model/
│   └── xgb_model.pkl           ← Trained XGBoost model
├── notebooks/
│   └── loan_model_dev.ipynb    ← Model training & dev
└── README.md
---

## 🧪 Features Used

- Gender
- Marital Status
- Dependents
- Education
- Employment Status
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

---

## ⚙️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/loan-approval-predictor.git
cd loan-approval-predictor

📊 Output Sample

✅ Approved | ❌ Rejected — based on the model’s prediction.

Also logged in prediction_log.csv with each session’s inputs + prediction.
---

## 👨‍💻 Author

**Vishal Singh**  
Aspiring Data Scientist & ML Engineer  
[LinkedIn](https://www.linkedin.com/in/yourprofile) | [Twitter](https://twitter.com/yourhandle) | [GitHub](https://github.com/yourusername)
