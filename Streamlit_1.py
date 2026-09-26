import streamlit as st
st.title("Heart Disease Prediction App")
age = st.number_input("Enter your age",min_value=0,max_value=120)
sex = st.selectbox("Sex",["Male","Female"])
cp = st.selectbox("Chest Pain Type",["Typical Angina","Atypical Angina","Non-anginal pain","Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure",min_value=80,max_value=200)
chol = st.number_input("Cholestrol",min_value=100,max_value=600)
