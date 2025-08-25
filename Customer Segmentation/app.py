import streamlit as st
import pandas as pd
import pickle

# --------------------------
# Load Pickled Models
# --------------------------
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

with open('cluster_labels.pkl', 'rb') as f:
    cluster_labels = pickle.load(f)

# --------------------------
# Streamlit App UI
# --------------------------
st.title("Customer Segmentation Predictor")
st.write("Enter the customer details to predict their segment:")

# Input form
with st.form(key='customer_form'):
    education = st.selectbox("Education", ["PhD", "Master", "Graduation", "Basic"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Together", "Divorced", "Widow", "Alone", "YOLO"])
    income = st.number_input("Income", min_value=0, value=50000)
    recency = st.number_input("Recency (days since last purchase)", min_value=0, value=10)
    num_web_visits = st.number_input("Number of Web Visits per Month", min_value=0, value=3)
    complain = st.number_input("Complain (0 or 1)", min_value=0, max_value=1, value=0)
    total_spendings = st.number_input("Total Spendings", min_value=0, value=400)
    age = st.number_input("Age", min_value=0, value=35)
    total_children = st.number_input("Total Children", min_value=0, value=1)
    total_purchases = st.number_input("Total Purchases", min_value=0, value=10)
    total_campaigns_accepted = st.number_input("Total Campaigns Accepted", min_value=0, value=1)
    
    submit_button = st.form_submit_button(label='Predict Cluster')

# --------------------------
# Prediction
# --------------------------
if submit_button:
    new_data = pd.DataFrame([{
        'Education': education,
        'Marital_Status': marital_status,
        'Income': income,
        'Recency': recency,
        'NumWebVisitsMonth': num_web_visits,
        'Complain': complain,
        'Total_Spendings': total_spendings,
        'Age': age,
        'Total_Children': total_children,
        'Total_Purchases': total_purchases,
        'Total_Campaigns_Accepted ': total_campaigns_accepted
    }])
    
    # Transform and predict
    X_new = preprocessor.transform(new_data)
    cluster_pred = kmeans.predict(X_new)
    cluster_label_pred = [cluster_labels[c] for c in cluster_pred]

    #cluster_label_pred = []
    #for c in cluster_pred:
    #    cluster_label_pred.append(cluster_labels[c])

    
    
    st.success(f"The customer belongs to cluster {cluster_pred[0]}: **{cluster_label_pred[0]}**")
