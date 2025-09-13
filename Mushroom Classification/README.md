# 🍄 Mushroom Classification - Multi-Model ML Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-99%25-brightgreen?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-blue?style=for-the-badge&logo=python&logoColor=white" alt="Optuna"/>
  <img src="https://img.shields.io/badge/Python-3.10-orange?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

## 📝 Overview
This project builds a **robust machine learning pipeline** to classify mushrooms as **edible (e)** or **poisonous (p)** using a Kaggle dataset. It combines **data preprocessing, feature encoding, multiple ML models, and hyperparameter optimization using Optuna**. The pipeline outputs predictions for submission and evaluates model performance with accuracy and ROC-AUC score.

## 🗂 Dataset
- **Train Dataset:** `train.csv`  
- **Test Dataset:** `test.csv`  
- **Sample Submission:** `sample_submission.csv`  

Dataset source: [Kaggle Mushroom Classification](https://www.kaggle.com/competitions/playground-series-s4e8)
                [Kaggle Mushroom Dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification)

## ⚡ Features
- 22 columns including cap, gill, stem, veil, ring, spore, habitat, and season.
- Target column: `class` (`e` or `p`)

## 🛠 Key Steps
1. **Load data** and drop columns with high missing values.
2. **Train-validation split** for model evaluation.
3. **Preprocessing pipeline**:
   - Categorical: `OrdinalEncoder` + `SimpleImputer`  
   - Numerical: `StandardScaler` + `SimpleImputer`
4. **Hyperparameter tuning** using Optuna for multiple models:
   - Logistic Regression, Random Forest, XGBoost, SVM, Gradient Boosting, LightGBM, CatBoost, KNN
5. **Cross-validation** to evaluate model performance.
6. **Final model training** on full training dataset.
7. **Predictions** on test dataset.
8. **ROC curve** and **best threshold calculation**.
9. **Submission file** generation.

## 🔧 Libraries Used
```python
pandas
numpy
scikit-learn
xgboost
lightgbm
catboost
optuna
matplotlib

```

# 📊 Model Performance
- **Validation Accuracy:** 99%  
- **ROC-AUC:** 0.99  
- Compared multiple models using Optuna to select the best hyperparameters.

## 🚀 Usage
Clone the repo:
```bash
git clone https://github.com/yourusername/mushroom-classification.git

```

# Install required packages:

```bash
pip install -r requirements.txt

```

# Run the notebook:

Mushroom_final.ipynb

Run it on Jupyter Notebook or Kaggle.

The final file submission.csv will be generated with predicted classes (e / p).

## 📈 ROC Curve & Threshold

- ROC curve plotted for validation set.
- Optimal threshold selected using Youden's J statistic.
- Predictions adjusted for the best threshold to improve classification.

## 📂 File Structure

├── train.csv
├── test.csv
├── sample_submission.csv
├── Mushroom_final.ipynb
├── requirements.txt
└── README.md 

## 💡 Notes
- Fully automated pipeline for preprocessing, model selection, and hyperparameter tuning.
- Compatible with large categorical datasets, handles missing values, and avoids errors in Windows parallel execution.
- Customizable: Add/remove models in Optuna search or adjust preprocessing steps.

## 📌 Author
**Kaustav Roy Chowdhury**

<p align="center"> Made with ❤️ using Python & Scikit-Learn </p>