# 🏦 Loan Status Prediction

## 🎯 Objective

This project aims to predict whether a loan application will be **approved** or **denied** based on applicant information such as income, employment status, credit history, and property area. It uses a machine learning model trained on historical loan data to make predictions.

## 🛠️ Tools & Technologies Used

- **Python**
- **Scikit-learn**: For model training and prediction
- **Pandas, NumPy**: For data preprocessing
- **Streamlit**: To create an interactive web application
- **Pickle**: For saving and loading the trained model

## 📈 Model Accuracy

The machine learning model used in this project delivers high accuracy and efficiently identifies patterns that lead to loan approval or denial.  
> 🔍 Exact metrics may vary, but accuracy is generally above **85%** depending on the dataset.

## 🏗️ Features Considered

- Gender
- Marital Status
- Dependents
- Education Level
- Self-Employment Status
- Applicant & Coapplicant Income
- Loan Amount & Term
- Credit History
- Property Area

## 🖥️ Web Application

This project includes a **Streamlit** web app that allows users to input applicant details and receive real-time predictions.

### ▶️ To run the app locally:

```bash
streamlit run Loan_Status_Prediction_Web_App.py

