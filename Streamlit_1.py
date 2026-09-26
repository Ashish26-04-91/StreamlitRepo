import streamlit as st
import pickle
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
with open("/mount/src/streamlitrepo/classifier.pkl", "rb") as f:
    model = pickle.load(f)
with open("/mount/src/streamlitrepo/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)      
    
st.title("Heart Disease Prediction App")
st.set_page_config(page_title = "Heart Disease Predictor",page_icon = "❤️")
age = st.number_input("Enter your age",min_value=0,max_value=120,value=50)
sex = st.selectbox("Sex",["Male","Female"])
cp = st.selectbox("Chest Pain Type",["Typical Angina","Atypical Angina","Non-anginal pain","Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure",min_value=80,max_value=200,value = 120)
chol = st.number_input("Cholestrol",min_value=100,max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",["Yes","No"])
restecg = st.selectbox("Resting ECG",["Normal","ST-T wave abnormality","Left ventricular hypertrophy"])
thalach = st.number_input("Max Heart Rate Achieved",min_value=60,max_value=220,value=150)
exang = st.selectbox("Exercise Induced Angina",["Yes","No"])
oldpeak = st.number_input("ST Depression",min_value=0.0,max_value=6.0,value = 1.0)
slope = st.selectbox("Slope of Peak Exercise",["Upsloping","Flat","Downsloping"])
ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", ["Normal", "Fixed defect", "Reversible defect"])

if sex == "Male":
   sex = 1
elif sex == "Female":
   sex = 0


if cp == "Typical Angina":
   cp  = 0
elif cp == "Atypical Angina":
    cp = 1
elif cp == "Non-anginal pain":
    cp = 2
elif cp == "Asymptomatic":
    cp = 3

if fbs =="Yes":
    fbs = 1
elif fbs == "No":
    fbs = 0
    

if restecg == "Normal":
   restecg = 0
elif restecg == "ST-T wave abnormality":
    restecg = 1
elif restecg == "Left ventricular hypertrophy":
    restecg = 2

if exang =="Yes":
    exang = 1
elif exang == "No":
    exang = 0


if slope == "Upsloping":
    slope = 0
elif slope == "Flat":
    slope = 1
elif slope == "Downsloping":
    slope = 2

if thal == "Normal":
    thal = 1
elif thal == "Fixed defect":
    thal = 2
elif thal == "Reversible defect":
    thal = 3
if st.button("Predict"):
    scale = MinMaxScaler()
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    input_data[:,[3,4,7]] = scaler.fit_transform(input_data[:,[3,4,7]])
    prediction = model.predict(input_data)
    result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
    st.success(result)
