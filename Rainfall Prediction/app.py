import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------
# Load trained model
# -----------------------------
with open("rainfall_model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Rainfall Predictor",
    page_icon="☔",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# App Header
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #1E90FF;'>☔ Rainfall Predictor</h1>
    <p style='text-align: center; font-size: 18px;'>Predict whether it will rain based on weather conditions!</p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# -----------------------------
# User Input with columns for layout
# -----------------------------
def user_input_features():
    col1, col2 = st.columns(2)
    
    with col1:
        pressure = st.number_input("🧭 Pressure", value=1015.0)
        dewpoint = st.number_input("🌡️ Dewpoint", value=15.0)
        humidity = st.number_input("💧 Humidity (%)", value=70.0)
        cloud = st.number_input("☁️ Cloud Cover", value=50.0)

    with col2:
        sunshine = st.number_input("☀️ Sunshine", value=5.0)
        winddirection = st.number_input("🧭 Wind Direction (Degrees)", value=90.0)
        windspeed = st.number_input("🌬️ Wind Speed", value=15.0)

    data = {
        "pressure": [pressure],
        "dewpoint": [dewpoint],
        "humidity": [humidity],
        "cloud": [cloud],
        "sunshine": [sunshine],
        "winddirection": [winddirection],
        "windspeed": [windspeed]
    }
    return pd.DataFrame(data)

input_df = user_input_features()

# -----------------------------
# Transform wind direction into cyclical features
# -----------------------------
input_df['wind_dir_sin'] = np.sin(np.deg2rad(input_df['winddirection']))
input_df['wind_dir_cos'] = np.cos(np.deg2rad(input_df['winddirection']))
input_df = input_df.drop(columns=['winddirection'])

# -----------------------------
# Predict button
# -----------------------------
if st.button("🔮 Predict"):
    # Align columns with trained model features
    input_df = input_df[model.feature_names_in_]

    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[:,1][0]

    st.markdown("---")
    st.write(f"Prediction Probability of Rain: {probability:.2f}")

    if prediction == 1:
        st.success("🌧️ Prediction: It **will rain**!")
    else:
        st.info("☀️ Prediction: It **will not rain**!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Created by <b>Kaustav Roy Chowdhury</b></p>",
    unsafe_allow_html=True
)
