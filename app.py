import streamlit as st
import pandas as pd
import pickle

# ========================
# Custom function for pipeline
# ========================
binary_yn = ["default", "housing", "loan"]

def map_yes_no(df):
    mapping = {"yes": 1, "no": 0}
    out = df.copy()
    for c in binary_yn:
        out[c] = out[c].map(mapping).astype(int)
    return out

# ========================
# Load the trained pipeline
# ========================
with open("bank_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# ========================
# Streamlit UI
# ========================
st.title("Bank Subscription Prediction")
st.write("Enter customer details:")

# Numeric inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
balance = st.number_input("Balance", min_value=-10000, max_value=100000, value=1000)
day = st.number_input("Day of the month", min_value=1, max_value=31, value=15)
duration = st.number_input("Call duration (seconds)", min_value=0, max_value=5000, value=200)
campaign = st.number_input("Number of contacts", min_value=1, max_value=50, value=1)
pdays = st.number_input("Days since last contact", min_value=-1, max_value=1000, value=-1)
previous = st.number_input("Previous contacts", min_value=0, max_value=50, value=0)

# Categorical inputs
job = st.selectbox("Job", ["admin.","blue-collar","entrepreneur","housemaid","management",
                           "retired","self-employed","services","student","technician","unemployed","unknown"])
marital = st.selectbox("Marital", ["divorced","married","single"])
education = st.selectbox("Education", ["unknown","primary","secondary","tertiary"])
default = st.selectbox("Has credit in default?", ["yes","no"])
housing = st.selectbox("Has housing loan?", ["yes","no"])
loan = st.selectbox("Has personal loan?", ["yes","no"])
contact = st.selectbox("Contact communication type", ["cellular","telephone"])
month = st.selectbox("Last contact month", ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
poutcome = st.selectbox("Outcome of previous campaign", ["failure","nonexistent","success"])

# Create input DataFrame
input_df = pd.DataFrame({
    "age": [age],
    "balance": [balance],
    "day": [day],
    "duration": [duration],
    "campaign": [campaign],
    "pdays": [pdays],
    "previous": [previous],
    "job": [job],
    "marital": [marital],
    "education": [education],
    "default": [default],
    "housing": [housing],
    "loan": [loan],
    "contact": [contact],
    "month": [month],
    "poutcome": [poutcome]
})

# Predict button
if st.button("Predict"):
    pred = model.predict(input_df)
    pred_proba = model.predict_proba(input_df)[0][1]  # probability of "yes"
    st.success(f"Prediction: {pred[0]}")
    st.info(f"Probability of subscribing: {pred_proba:.2f}")
