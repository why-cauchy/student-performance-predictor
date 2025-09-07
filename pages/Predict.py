import streamlit as st
import joblib

# Load ML model
model = joblib.load("student_model.pkl")

st.title("📊 Predict Student Performance")
st.write("Enter details below to predict the final grade:")

col1, col2 = st.columns(2)
with col1:
    study_time = st.number_input("Study Time (hours)", 1, 10, 5)
    absences = st.number_input("Absences", 0, 30, 2)
with col2:
    g1 = st.number_input("Grade 1", 0, 20, 10)
    g2 = st.number_input("Grade 2", 0, 20, 10)

if st.button("🔮 Predict Now"):
    pred = model.predict([[study_time, absences, g1, g2]])
    st.success(f"✅ Predicted Final Grade: **{pred[0]}**")
