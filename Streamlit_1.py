import streamlit as st
st.title("Hello, Mamta!")
st.title("Gudde ko lekr mandir chalna hai kya aaj.")
select_time = st.selectbox("Please select your time",["---Select time---","6 pm","7 pm","8 pm"])
if select_time != "---Select time---":
  st.write("okay be ready at", select_time)
