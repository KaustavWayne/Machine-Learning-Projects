# 🌧️ Rainfall Prediction ML Pipeline  

<p align="center">
  <img src="https://img.shields.io/badge/Rainfall_Prediction-DeepSkyBlue?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Rainfall Prediction" width="600"/>
</p>

<p align="center">
  <em>"Predict the rain before it falls – harnessing the power of Machine Learning!"</em>
</p>

---

## 📖 Overview  
This project builds a **Rainfall Prediction Machine Learning Pipeline** using:  

- **Imbalanced data handling** with RandomOverSampler 🌍  
- **Feature scaling** using StandardScaler 📊  
- **Models**: Logistic Regression, Random Forest, and XGBoost 🌲⚡  
- **Evaluation**: ROC-AUC, Accuracy, Classification Report, Confusion Matrix ✅  

The model predicts whether it will **rain tomorrow or not** based on meteorological data such as wind speed, wind direction, and temperature.  

---

## 📂 Dataset  
- **File**: `Rainfall.csv`  
- **Target**: `rainfall` (0 = No Rain, 1 = Rain)  
- Features include temperature, wind speed, wind direction, etc.  

<p align="center">
  <img src="https://user-images.githubusercontent.com/00000000/weather-data-sample.png" alt="Rainfall Dataset Sample" width="600"/>
</p>

---

## ⚙️ Methodology  

1️⃣ **Data Preprocessing**  
- Handle missing values  
- Encode categorical variables  
- Scale numerical features  

2️⃣ **Class Imbalance Fix**  
- Applied **RandomOverSampler** to balance minority rainfall class  

3️⃣ **Model Training**  
- Logistic Regression  
- Random Forest  
- XGBoost  

4️⃣ **Evaluation Metrics**  
- ROC-AUC Curve  
- Accuracy (Direct & Threshold-based)  
- Confusion Matrix  

<p align="center">
  <img src="https://user-images.githubusercontent.com/00000000/roc-curve.png" alt="ROC Curve Example" width="500"/>
</p>  

---

## 📊 Results  

| Model                | ROC-AUC | Accuracy (Threshold) | Accuracy (Direct) |
|-----------------------|---------|-----------------------|-------------------|
| Logistic Regression  | ~0.82   | ~0.80                 | ~0.78             |
| Random Forest        | ~0.88   | ~0.85                 | ~0.84             |
| XGBoost              | ~0.90   | ~0.86                 | ~0.85             |

> *"Random Forest and XGBoost consistently outperformed Logistic Regression for rainfall classification."*  

---

## 🚀 How to Run  

```bash
# Clone the repository
git clone https://github.com/your-username/rainfall-prediction.git

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python rainfall_prediction.py


## 🌟 Future Scope  

- Deploy using **Streamlit / Flask** for live predictions  
- Hyperparameter tuning with **GridSearchCV**  
- Feature engineering using domain weather knowledge

```

---

## 👨‍💻 Author  

**Kaustav Roy Chowdhury**  

<p align="center"> 
  <em>"Code is like rainfall – sometimes it floods you with bugs, but when it flows right, it nourishes the world 🌧️💻"</em> 
</p>

