# ❤️ Heart Disease Risk Prediction

## 🎯 Objective

This project aims to predict the **risk of heart disease** in individuals based on various health and lifestyle parameters. Using machine learning techniques, the model classifies whether a person is at **high risk** or **low risk** of developing heart disease.

## 🛠️ Tools & Technologies Used

- **Python**
- **Streamlit**: For building the interactive web application
- **Scikit-learn**: For model training and prediction
- **Pandas, NumPy**: For data preprocessing
- **Pickle**: To save and load the trained model and scaler

## 📈 Model Accuracy

The trained model, based on health and lifestyle features, achieves high accuracy in distinguishing between low-risk and high-risk individuals.  
> ⚠️ Exact accuracy value depends on the dataset and may vary slightly, but is generally above **90%**.

## 💡 Features Considered

- Age, Sex, Cholesterol, Heart Rate
- Diabetes, Smoking, Family History, Obesity
- Alcohol Consumption, Exercise Hours, Diet
- Previous Heart Problems, Medication Use
- Stress Level, Sedentary Hours, Income
- BMI, Triglycerides, Blood Pressure
- Physical Activity Days, Sleep Hours

## 🖥️ Web Application

The project includes a user-friendly **Streamlit web app** where users can enter their health parameters and get an instant risk prediction.

To run the app locally:

```bash
streamlit run heart_Disease_Risk_Predict_Web_App.py

