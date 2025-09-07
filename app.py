import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# ====================
# Load Model
# ====================
model = joblib.load("student_model.pkl")

# Load Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_student = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

# ====================
# Sidebar Navigation
# ====================
with st.sidebar:
    selected = option_menu(
        "📚 Student Predictor",
        ["🏠 Home", "📊 Predict", "ℹ️ About", "📩 Contact"],
        icons=["house", "bar-chart", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0
    )

# ====================
# Pages
# ====================

if selected == "🏠 Home":
    st.title("🎓 Student Performance Predictor")
    st.write("Welcome! This app helps predict student performance using Machine Learning.")
    st_lottie(lottie_student, height=300)
    st.info("Navigate using the sidebar to try predictions, learn about the project, or contact us.")

elif selected == "📊 Predict":
    st.title("📊 Predict Student Performance")
    st.write("Enter details below:")

    # Input fields
    hours = st.slider("Study Hours per Day", 0, 12, 4)
    attendance = st.slider("Attendance %", 0, 100, 75)
    assignments = st.slider("Assignments Completed (%)", 0, 100, 80)

    # Predict Button
    if st.button("🔮 Predict"):
        input_data = np.array([[hours, attendance, assignments]])
        prediction = model.predict(input_data)[0]
        st.success(f"✅ Predicted Performance: **{prediction}**")

elif selected == "ℹ️ About":
    st.title("ℹ️ About")
    st.write("""
    This web application uses a **Machine Learning model** 
    to predict student performance based on study habits, 
    attendance, and assignments.
    
    Built with ❤️ using Streamlit, Scikit-learn, and Python.
    """)

elif selected == "📩 Contact":
    st.title("📩 Contact Us")
    st.write("Got questions? Reach out!")
    st.write("📧 Email: support@yourapp.com")
    st.write("🌐 Website: [yourwebsite.com](http://yourwebsite.com)")
