# 🎵 Beats Per Minute (BPM) Prediction  

<p align="center">
  <img src="https://img.shields.io/badge/Competition-Kaggle_Playground_Series_S5E9-blue?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Competition"/>
  <img src="https://img.shields.io/badge/Model-Optuna_Hyperparameter_Tuning-green?style=for-the-badge&logo=python&logoColor=white" alt="Optuna"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-Scikit--Learn-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
</p>

---

## 📌 Overview  
This project tackles the **[Kaggle Playground Series - Season 5, Episode 9](https://www.kaggle.com/competitions/playground-series-s5e9)** competition, where the goal is to predict the **Beats Per Minute (BPM)** from audio-related features.  
The dataset was generated using a deep learning model trained on the BPM Prediction Challenge dataset. Feature distributions are similar but not identical to the original dataset.  

We leverage **Optuna for hyperparameter optimization** across multiple models (Logistic Regression, Random Forest, XGBoost, LightGBM, CatBoost, GradientBoosting, KNN, DecisionTree, Ridge, etc.) to maximize prediction performance.

---

## 📂 Dataset Description  

The dataset consists of train and test files:  

- **train.csv** → Training dataset containing features and target (`BeatsPerMinute`)  
- **test.csv** → Test dataset where BPM predictions need to be made  
- **sample_submission.csv** → Submission template in the correct format  

### ⚡ Key Points  
- Target variable: `BeatsPerMinute` (continuous numerical feature).  
- Generated via deep learning on the BPM Prediction Challenge dataset.  
- Original dataset can also be incorporated for performance boosts.  

---

## 🛠️ Project Workflow  

1. **Data Preprocessing**  
   - Handle missing values  
   - Feature scaling / encoding (if necessary)  

2. **Modeling**  
   - Classification and Regression handled separately  
   - Hyperparameter tuning via **Optuna**  
   - Models included:
     - Logistic Regression  
     - Ridge / Lasso / ElasticNet  
     - Random Forest  
     - Decision Tree  
     - Gradient Boosting  
     - XGBoost  
     - LightGBM  
     - CatBoost  
     - KNN  

3. **Evaluation Metrics**  
   - Classification → `Accuracy`  
   - Regression → `R² Score`  

4. **Cross Validation**  
   - 3-Fold CV used to ensure robust performance estimation  

---

## 🚀 Tech Stack  

- **Programming Language:** Python 🐍  
- **Libraries:**  
  - Optuna (Hyperparameter Tuning)  
  - Scikit-learn (Modeling & CV)  
  - XGBoost, LightGBM, CatBoost (Boosting Models)  
  - NumPy & Pandas (Data Handling)  

---

## 📊 Results  

- Automated Optuna search for best hyperparameters  
- Improved BPM prediction accuracy & regression performance  
- Ready-to-submit Kaggle predictions  

---

## 📎 Competition Link  

👉 [Kaggle - Playground Series S5E9](https://www.kaggle.com/competitions/playground-series-s5e9)

---

## 👨‍💻 Author  

- **Kaustav Roy Chowdhury**  
