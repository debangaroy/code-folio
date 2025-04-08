# 🧠 Parkinson's Disease Risk Prediction

## 🎯 Objective
This project aims to detect **Parkinson’s Disease** in individuals using **machine learning** based on 22 vocal frequency-related biomedical features. A user-friendly web app, built with **Streamlit**, allows for real-time prediction by taking biomedical input and providing instant results.

---

## 🛠️ Tools & Technologies Used
- **Python**
- **Scikit-learn** – Model training & evaluation
- **Pandas, NumPy** – Data preprocessing
- **Pickle** – Model & scaler serialization
- **Streamlit** – Web interface for real-time predictions

---

## 📊 Features (Biomedical Attributes)
The model uses the following 22 features extracted from voice recordings:
- **MDVP**: Fo(Hz), Fhi(Hz), Flo(Hz), Jitter(%), Jitter(Abs), RAP, PPQ
- **Shimmer**: Shimmer, Shimmer(dB), APQ3, APQ5, APQ, DDA
- **Others**: NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE

These features help capture variations in vocal cord behavior, which are often indicators of Parkinson’s Disease.

---

## 🤖 Machine Learning Model
- **Model Used**: Support Vector Machine (SVM) with a linear kernel
```python
model = SVC(kernel="linear")
model.fit(X_train, y_train)

---
## ✅ Model Accuracy & Evaluation
Accuracy: 87.18%
