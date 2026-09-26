import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
model = pickle.load(open("classifier.pkl","rb"))
st.title("Heart Disease Prediction App")
age = st.number_input("Enter your age",min_value=0,max_value=120,value=50)
sex = st.selectbox("Sex",["Male","Female"])
cp = st.selectbox("Chest Pain Type",["Typical Angina","Atypical Angina","Non-anginal pain","Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure",min_value=80,max_value=200,value = 120)
chol = st.number_input("Cholestrol",min_value=100,max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",["Yes","No")
restecg = st.selectbox("Resting ECG",["Normal","ST-T wave abnormality","Left ventricular hypertrophy"])
thalach = st.number_input("Max Heart Rate Achieved",min_value=60,max_value=220,value=150)
exang = st.selectbox("Exercise Induced Angina",["Yes","No"])
oldpeak = st.number_input("ST Depression",min_value=0.0,max_value=6.0,value = 1.0)
slope = st.selectbox("Slope of Peak Exercise",["Upsloping","Flat","Downsloping"])
ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", ["Normal", "Fixed defect", "Reversible defect"])
if st.button("Predict"):
    scale = MinMaxScaler()
    trestbps = scale.fit_transform(trestbps)
    chol = scale.fit_transform(chol)
    thalach = scale.fit_transform(thalach)
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
    st.success(result)
