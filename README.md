# Bank Subscription Predictor 💰

<p align="center">
  <img src="https://img.shields.io/badge/Bank_Subscription_Predictor-LightBlue?style=for-the-badge&logo=streamlit&logoColor=white" alt="Bank Subscription Predictor" width="600"/>
</p>

<p align="center">
  <a href="https://www.kaggle.com/competitions/playground-series-s5e8/data">
    <img src="https://img.shields.io/badge/Dataset-Kaggle%20S5E8-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Dataset"/>
  </a>
</p>

<p align="center">
  <em>"Predict whether a client will subscribe to a bank term deposit using Machine Learning and Streamlit!"</em>
</p>

---

## Overview
This project predicts whether a client will subscribe to a term deposit based on bank marketing data. It leverages a **full ML pipeline** that includes preprocessing of categorical and numerical features and an **XGBoost classifier** for accurate predictions. The model is deployed as an interactive **Streamlit web app** for real-time user input and predictions.

## Dataset
- Kaggle: [Playground Series — Season 5, Episode 8 (Data)](https://www.kaggle.com/competitions/playground-series-s5e8/data)

---

## Features
- **Binary Features:** `default`, `housing`, `loan` (mapped to 0/1)  
- **Ordinal Features:** `education`, `month` (encoded with a defined order)  
- **Nominal Features:** `job`, `marital`, `contact`, `poutcome` (one-hot encoded)  
- **Numerical Features:** `age`, `balance`, `day`, `duration`, `campaign`, `pdays`, `previous`  
- **Target:** `y` (client subscription: yes/no)  

---

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/bank-subscription-predictor.git
cd bank-subscription-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## How It Works
1. The user inputs customer details via the Streamlit app.
2. The pipeline automatically preprocesses inputs (binary mapping, ordinal & one-hot encoding, scaling).
3. The trained XGBoost model predicts subscription (yes/no) and probability.
4. The app displays results interactively.

## Sample Screenshot
<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/bank-subscription-predictor/main/images/bank_app_screenshot.png" width="700"/>
</p>

## Model Evaluation
The XGBoost model was evaluated using 5-fold cross-validation:

| Metric | Score |
|---|---|
| Validation Accuracy | 0.88 |
| Test Accuracy | 0.86 |
| Fit Assessment | ✅ Good Fit |

## Tech Stack
- Python 🐍
- Scikit-learn 🛠️
- XGBoost ⚡
- Streamlit 🌐
- Pandas & NumPy 📊

## Author
Kaustav Roy Chowdhury  
GitHub | LinkedIn

## Dev Quotes
> "All models are wrong, but some are useful." — George E. P. Box

> "In God we trust; all others must bring data." — W. Edwards Deming

> "Premature optimization is the root of all evil." — Donald Knuth