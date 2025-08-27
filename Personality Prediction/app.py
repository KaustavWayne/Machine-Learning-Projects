import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load trained model
# -----------------------------
with open("personality_model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# App Header
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082;'>🧠 Personality Predictor</h1>
    <p style='text-align: center; font-size: 18px;'>Discover whether you are an Extrovert or Introvert!</p>
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
        Time_spent_Alone = st.selectbox("🕒 Time spent alone (hrs/day)", list(range(0, 21)))
        Stage_fear = st.selectbox("🎤 Stage fear?", ["No", "Yes"])
        Social_event_attendance = st.selectbox("🎉 Social event attendance", list(range(0, 11)))
        Going_outside = st.selectbox("🌳 Going outside", list(range(0, 11)))

    with col2:
        Drained_after_socializing = st.selectbox("😴 Drained after socializing?", ["No", "Yes"])
        Friends_circle_size = st.selectbox("👥 Friends circle size", list(range(0, 51)))
        Post_frequency = st.selectbox("📱 Post frequency", list(range(0, 11)))

    data = {
        "Time_spent_Alone": [Time_spent_Alone],
        "Stage_fear": [Stage_fear],
        "Social_event_attendance": [Social_event_attendance],
        "Going_outside": [Going_outside],
        "Drained_after_socializing": [Drained_after_socializing],
        "Friends_circle_size": [Friends_circle_size],
        "Post_frequency": [Post_frequency]
    }
    return pd.DataFrame(data)

input_df = user_input_features()

# -----------------------------
# Predict button
# -----------------------------
if st.button("🔮 Predict"):
    # Fix LightGBM feature names warning
    input_df = input_df[model.feature_names_in_]
    
    # Make prediction
    prediction = model.predict(input_df)[0]

    st.markdown("---")
    if prediction == "Extrovert" or prediction == 0:
        st.success("🎉 You are an **Extrovert** person!")
    else:
        st.info("🌱 You are an **Introvert** person!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Created by <b>Kaustav Roy Chowdhury</b></p>",
    unsafe_allow_html=True
)
