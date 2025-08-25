# 🛍️ Customer Segmentation with KMeans Clustering  

## 📌 Overview  
This project applies **KMeans clustering** on a [Customer Segmentation Dataset](https://www.kaggle.com/datasets/vishakhdapat/customer-segmentation-clustering) 
to segment users into meaningful groups based on **income** and **spending score**.  

The analysis is wrapped in an **interactive Streamlit app**, allowing businesses to:  
- Explore customer clusters visually  
- Predict which segment a new customer belongs to  
- Gain data-driven insights for targeted marketing strategies  


---

## 🎯 Objectives  
- Perform **data cleaning & preprocessing**  
- Apply **feature engineering** for clustering  
- Use **KMeans with Elbow Method & Silhouette Score** to find the best K  
- Analyze and label clusters into business-friendly categories  
- Deploy an **interactive Streamlit dashboard** for visualization & prediction  

---

## 🏗️ Project Workflow  

1. **Data Preparation**  
   - Handle missing values  
   - Scale numerical features  
   - Encode categorical features  

2. **Exploratory Data Analysis (EDA)**  
   - Distribution of income & spending  
   - Outlier detection using IQR  
   - Correlation heatmaps  

3. **KMeans Clustering**  
   - Elbow Method for optimal K  
   - Silhouette Score validation  
   - PCA for 2D visualization  

4. **Cluster Analysis & Labeling**  
   - Assign meaningful labels:  
     - 💎 High-Value Customers  
     - 💼 Careful Spenders  
     - 🎯 Big Spenders on Budget  
     - 📉 Low-Value Customers  

5. **Streamlit Application**  
   - Upload or input customer data  
   - Visualize clusters with PCA plots  
   - Predict customer segment instantly  

---

<!--
## 📊 Visuals  

### 🔹 Elbow Method (Best K = 4)  
![Elbow Method](https://github.com/your-repo-link/elbow_method.png)  

### 🔹 PCA Cluster Visualization  
![Cluster Plot](https://github.com/your-repo-link/cluster_plot.png)  

### 🔹 Streamlit App Screenshot  
![Streamlit App](https://github.com/your-repo-link/streamlit_app.png)  
-->
  
---

## ⚡ Streamlit App Demo  
Run the app locally:  
```bash
streamlit run app.py

```

## 🛠️ Tech Stack  

- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- **Streamlit** for dashboard & deployment  
- **KMeans Clustering** for unsupervised ML  
- **PCA** for visualization  

---

## 🚀 Business Value  

✅ Target marketing campaigns based on customer segment  
✅ Optimize loyalty programs  
✅ Reduce customer churn by focusing on high-risk groups  
✅ Improve resource allocation for sales teams  

---

## 👨‍💻 Author  

**Kaustav Roy Chowdhury**  

> 💡 "Code less. Think more."  
> 📊 "Clustering is not just grouping data, it’s grouping people’s behavior."  
> 🚀 "Turning raw numbers into real business stories."  

