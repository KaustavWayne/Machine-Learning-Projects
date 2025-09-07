# 🐦 Twitter Sentiment Analysis  

<p align="center">
  <img src="https://img.shields.io/badge/Twitter_Sentiment_Analysis-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Sentiment Analysis" width="600"/>
</p>

<p align="center">
  <em>"The goal is not to build models. The goal is to solve problems with models."</em>
</p>

---

## ✨ Tech Stack & Tools  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLTK-154D65?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>

---

## 📌 Overview  

This project performs **Twitter Sentiment Analysis** to classify tweets into **Positive, Negative, or Neutral** sentiments.  
We preprocess text, build multiple ML models, and deploy the best one using **Streamlit**.  

---

## 🚀 Features  

- 🧹 Text Cleaning & Preprocessing (stopwords, stemming, hashtags, mentions removal)  
- 📊 Exploratory Data Analysis with Matplotlib & Seaborn  
- 🔤 WordClouds for Positive, Negative & Neutral tweets  
- 🤖 Multiple ML models trained (Naive Bayes, Logistic Regression, Random Forest, Voting Classifier)  
- 📈 Performance comparison with Accuracy & Precision metrics  
- 🌐 Streamlit Web App for live sentiment prediction  

---

## ⚙️ Installation  

```bash
# Clone the repo
git clone https://github.com/your-username/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
🖥️ Usage
bash
Copy code
# Run the Streamlit app
streamlit run app.py
Enter a tweet in the textbox, and the model will classify it into:
✅ Positive | ❌ Negative | 😐 Neutral

📊 Model Performance
Model	Accuracy	Precision
Naive Bayes (MNB)	79%	0.78
Logistic Regression	82%	0.81
Random Forest	80%	0.79
Voting Classifier	84%	0.83

🚀 Deployment
🌐 Streamlit Cloud

☁️ Heroku / AWS / GCP (optional future scope)

👨‍💻 Author
Kaustav Roy Chowdhury

<p align="center"> <em>"Code is like rainfall – sometimes it floods you with bugs, but when it flows right, it nourishes the world 🌧️💻"</em> </p> ```