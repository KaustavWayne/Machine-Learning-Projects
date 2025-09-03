# 🥗 Obesity & CVD Risk Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Obesity_CVD_Predictor-Orange?style=for-the-badge&logo=python&logoColor=white" alt="Obesity CVD Predictor" width="600"/>
</p>

<p align="center">
  <em>"Predict Obesity/CVD risk categories using Machine Learning with XGBoost and LightGBM!"</em>
</p>

---

## 📖 Project Overview

This project focuses on predicting obesity or cardiovascular disease risk categories using a synthetic dataset from the **Kaggle Playground Series S4E2** competition. The dataset contains demographic, lifestyle, and health-related features.

**Key Objectives:**
- Classify individuals into risk categories (`NObeyesdad`)
- Implement machine learning pipelines with preprocessing and hyperparameter tuning
- Evaluate model performance and generate predictions for submission

---

## 🧰 Technologies & Libraries

| Category       | Tools/Libraries                                                                 |
|----------------|---------------------------------------------------------------------------------|
| **Core**       | Python 3.x, Pandas, NumPy                                                      |
| **ML Frameworks** | Scikit-learn, XGBoost (`XGBClassifier`), LightGBM (`LGBMClassifier`)          |
| **Preprocessing** | ColumnTransformer, Label Encoding, OneHotEncoder, StandardScaler              |
| **Tuning**     | GridSearchCV, RandomizedSearchCV                                               |
| **Visualization** | Matplotlib, Seaborn                                                           |
| **Utilities**  | Warnings suppression for cleaner outputs                                       |

---

## 🗂 Dataset

### **Files Used**
| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `train.csv`           | Training data with features and target           |
| `test.csv`            | Test data (no target values)                     |
| `sample_submission.csv` | Submission template for Kaggle                  |

### **Target Variable**
`NObeyesdad` – Categorical risk levels (e.g., `Insufficient_Weight`, `Obesity_Type_I`).

### **Feature Engineering**
- **Binary Columns** (e.g., `Gender`, `Smoke`): Mapped to `0/1`
- **Categorical Columns**: OneHotEncoded or OrdinalEncoded
- **Numerical Columns**: StandardScaled

---

## 🧹 Data Preprocessing Pipeline

1. **Target Encoding**: Label encoding for `NObeyesdad`
2. **Binary Features**: Converted to numerical (`Yes`→1, `No`→0)
3. **Categorical Features**: Encoded via `OneHotEncoder`/`OrdinalEncoder`
4. **Numerical Features**: Scaled using `StandardScaler`
5. **Pipeline Integration**: Combined using `ColumnTransformer`

---

## ⚙️ Machine Learning Workflow

### **Models**
- **XGBoost Classifier**
- **LightGBM Classifier**

### **Hyperparameter Tuning**
- **RandomizedSearchCV**: Fast exploration of hyperparameter space
- **GridSearchCV**: Fine-tuned optimization

### **Evaluation Metrics**
- Cross-validation accuracy
- Validation set accuracy
- Fit status (Overfitting/Underfitting/Good Fit)

---

## 📊 Results & Submission

- **Best Model**: Selected based on validation accuracy
- **Final Training**: Refitted on full training data
- **Submission**: Predictions saved to `submission.csv` for Kaggle:

```python
submission = pd.DataFrame({
    "id": test["id"],
    "NObeyesdad": final_preds
})
submission.to_csv("submission.csv", index=False)
```

---

## 🔮 Future Enhancements

- **Feature Engineering**: Capture lifestyle patterns
- **Ensemble Methods**: Combine XGBoost & LightGBM
- **Explainability**: SHAP/LIME for model interpretation
- **Deployment**: Web app via Streamlit/Flask

---

<p align="center">
  <em>“Predicting health risks intelligently using Machine Learning pipelines!”</em>
</p>
```

### Key Improvements:
1. **Structured Tables**: Better readability for technologies and dataset files.
2. **Consistent Formatting**: Uniform headers and bullet points.
3. **Code Block**: Properly formatted Python snippet for submission.
4. **Visual Hierarchy**: Clear section breaks with emojis.

---

