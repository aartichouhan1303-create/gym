# 🚀 Streamlit UI Code for Gym Members Exercise Predict
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Gym Exercise Prediction",
    page_icon="🏋️",
    layout="wide"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    model = joblib.load("linear_model.pkl")
    return model

model = load_model()

# ================= TITLE =================
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🏋️ Gym Members Exercise Prediction App</h1>
    <p style='text-align: center;'>Predict calories burned using Machine Learning</p>
""", unsafe_allow_html=True)

st.write("---")

# ================= SIDEBAR =================
st.sidebar.header("Enter User Details")

age = st.sidebar.slider("Age", 15, 80, 25)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", 30.0, 200.0, 70.0)
height = st.sidebar.number_input("Height (m)", 1.0, 2.5, 1.70)
max_bpm = st.sidebar.slider("Max BPM", 100, 220, 180)
avg_bpm = st.sidebar.slider("Average BPM", 50, 200, 140)
resting_bpm = st.sidebar.slider("Resting BPM", 40, 100, 60)
session_duration = st.sidebar.slider("Session Duration (hours)", 0.5, 5.0, 1.0)

workout_type = st.sidebar.selectbox(
    "Workout Type",
    ["Cardio", "HIIT", "Strength", "Yoga"]
)

fat_percentage = st.sidebar.slider("Fat Percentage", 5.0, 50.0, 20.0)
water_intake = st.sidebar.slider("Water Intake (liters)", 1.0, 10.0, 3.0)
workout_frequency = st.sidebar.slider("Workout Frequency (days/week)", 1, 7, 3)
experience_level = st.sidebar.slider("Experience Level", 1, 3, 1)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 22.0)

# ================= ENCODING =================
gender_encoded = 1 if gender == "Male" else 0

workout_map = {
    "Cardio": 0,
    "HIIT": 1,
    "Strength": 2,
    "Yoga": 3
}

workout_encoded = workout_map[workout_type]

# ================= INPUT DATA =================
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender_encoded],
    'Weight (kg)': [weight],
    'Height (m)': [height],
    'Max_BPM': [max_bpm],
    'Avg_BPM': [avg_bpm],
    'Resting_BPM': [resting_bpm],
    'Session_Duration (hours)': [session_duration],
    'Workout_Type': [workout_encoded],
    'Fat_Percentage': [fat_percentage],
    'Water_Intake (liters)': [water_intake],
    'Workout_Frequency (days/week)': [workout_frequency],
    'Experience_Level': [experience_level],
    'BMI': [bmi]
})

# ================= PREDICTION =================
if st.button("Predict Calories Burned 🔥"):
    prediction = model.predict(input_data)

    st.success(f"Estimated Calories Burned: {prediction[0]:.2f} kcal")

    st.balloons()

# ================= SHOW DATA =================
st.write("---")
st.subheader("📊 Input Data")
st.dataframe(input_data)

# ================= FOOTER =================
st.write("---")
st.markdown(
    "<center>Made with ❤️ using Streamlit & Machine Learning</center>",
    unsafe_allow_html=True
)


