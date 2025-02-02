import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_filename = 'O:/Projects/Loan Status Prediction/trained_Loan_Status_Prediction_model.sav'
classifier = pickle.load(open(model_filename, 'rb'))

# Function to make predictions
def predict_loan_status(gender, married, dependents, education, self_employed, 
                        applicant_income, coapplicant_income, loan_amount, 
                        loan_amount_term, credit_history, property_area):
    
    # Convert inputs to a format that the model can understand
    data = np.array([[gender, married, dependents, education, self_employed,
                      applicant_income, coapplicant_income, loan_amount,
                      loan_amount_term, credit_history, property_area]])
    
    # Predict loan status
    prediction = classifier.predict(data)
    
    # Return prediction (1 = Approved, 0 = Not Approved)
    return prediction[0]

# Streamlit app UI
st.title("Loan Status Prediction")

st.write("""
# Enter the details below to predict the loan status (Approved/Denied)
""")

# Collect user inputs for loan application
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Marital Status', ['Married', 'Not Married'])
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income', min_value=0)
coapplicant_income = st.number_input('Coapplicant Income', min_value=0)
loan_amount = st.number_input('Loan Amount', min_value=0)
loan_amount_term = st.selectbox('Loan Amount Term (in months)', ['12', '24', '36', '60', '180', '240'])
credit_history = st.selectbox('Credit History', ['1.0', '0.0'])
property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

# Convert input data to required numerical values
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Married' else 0
dependents = 4 if dependents == '3+' else int(dependents)
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
loan_amount_term = int(loan_amount_term)
credit_history = 1.0 if credit_history == '1.0' else 0.0
property_area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[property_area]

# Button to trigger prediction
if st.button('Predict Loan Status'):
    prediction = predict_loan_status(gender, married, dependents, education, self_employed, 
                                     applicant_income, coapplicant_income, loan_amount, 
                                     loan_amount_term, credit_history, property_area)
    
    if prediction == 1:
        st.success('Loan Approved!')
    else:
        st.error('Loan Denied!')

# Run the app in a new terminal
# python -m streamlit run Loan_Status_Prediction_Web_App.py
