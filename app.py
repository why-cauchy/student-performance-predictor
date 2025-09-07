import streamlit as st
import joblib

# Load ML model
model = joblib.load("student_model.pkl")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📊 Predict", "ℹ️ About", "📞 Contact Us"])

# ---------------- Home Page ----------------
if page == "🏠 Home":
    st.title("🎓 Student Performance Predictor")
    st.write(
        """
        Welcome to the **Student Performance Predictor** web app!  
        🚀 This tool uses Machine Learning to provide **educational insights** 
        and help understand how students might perform.  

        Use the sidebar to navigate:
        - 📊 Predict student grades
        - ℹ️ Learn more about the project
        - 📞 Contact us
        """
    )
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=180)

# ---------------- Prediction Page ----------------
elif page == "📊 Predict":
    st.title("📊 Predict Student Performance")
    st.write("Fill in the details below to get a grade prediction:")

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

# ---------------- About Page ----------------
elif page == "ℹ️ About":
    st.title("ℹ️ About This Project")
    st.write(
        """
        This web app is designed to predict **student performance** using 
        Machine Learning models trained on educational datasets.  

        **Tech Stack:**
        - 🐍 Python
        - 🤖 Scikit-Learn
        - 📊 Streamlit  

        Built with ❤️ to assist educators, institutions, and students.
        """
    )

# ---------------- Contact Page ----------------
elif page == "📞 Contact Us":
    st.title("📞 Contact Us")
    st.write("We’d love to hear from you! 💌")
    st.write("📧 Email: support@edupredictor.com")
    st.write("🌐 Website: www.edupredictor.com")
    st.write("📍 Location: Burewala, Pakistan")
