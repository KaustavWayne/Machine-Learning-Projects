# 🚀 Spaceship Titanic: Predicting Dimensional Transport  

> A Kaggle machine learning project to determine whether passengers aboard the Spaceship Titanic were transported to another dimension.  

---

## 📂 Project Structure

├── Space Titanic.ipynb # Main Jupyter Notebook with analysis & model
├── train.csv # Training dataset
├── test.csv # Test dataset
├── sample_submission.csv # Kaggle sample submission format
├── submission.csv # My model’s final submission
└── README.md # Project documentation


---

## 📖 Overview  

The **Spaceship Titanic** competition on Kaggle presents a futuristic dataset inspired by the Titanic disaster.  
Instead of an iceberg, passengers may mysteriously be **transported to another dimension**.  

Our task is to use machine learning to predict whether a passenger will be `Transported = True or False`,  
based on demographic, travel, and spending behavior data.  

---

## 🧾 Dataset Information  

- **PassengerId** → Unique ID (`gggg_pp`) identifying group and passenger number  
- **HomePlanet** → Passenger's planet of origin  
- **CryoSleep** → Whether the passenger chose suspended animation during the trip  
- **Cabin** → Format `deck/num/side` (e.g., F/33/P)  
- **Destination** → Intended destination planet  
- **Age** → Passenger’s age  
- **VIP** → Whether the passenger purchased VIP service  
- **RoomService, FoodCourt, ShoppingMall, Spa, VRDeck** → Amenity spending  
- **Name** → Passenger name  
- **Transported** → Target variable (True/False)  

---

## 🔍 Steps in the Project  

1. **Exploratory Data Analysis (EDA)**  
   - Passenger demographics distribution  
   - Spending behavior comparisons (Transported vs Not)  
   - Cabin & group insights  

   ![EDA Example](figures/eda_plot.png)  

2. **Feature Engineering**  
   - Splitting `Cabin` into `Deck`, `Number`, `Side`  
   - Creating `GroupSize` from `PassengerId`  
   - Aggregating spending into `TotalSpending`  

   ![Feature Engineering](figures/feature_eng.png)  

3. **Modeling & Evaluation**  
   - Baseline: Logistic Regression  
   - Tree Models: Random Forest, XGBoost, LightGBM  
   - Final model achieved **~79–80% accuracy**  

   ![Model Results](figures/model_results.png)  

4. **Submission**  
   - Generated `submission.csv` with predictions in the required Kaggle format  
   - Submitted to leaderboard ✅  

   ![Leaderboard](figures/leaderboard.png)  

---

## 📊 Results  

- **Validation Accuracy**: ~79%  
- **Final Kaggle Submission**: `submission.csv`  
- Positioned in the **top leaderboard range** for the Spaceship Titanic competition 🚀  

---

## 📌 How to Run  

1. Clone the repository or copy project files.  
2. Place `train.csv`, `test.csv`, and `sample_submission.csv` inside the root folder.  
3. Open `Space Titanic.ipynb` in Jupyter/Colab.  
4. Run all cells to train models and generate predictions.  
5. The final file `submission.csv` will be created for Kaggle submission.  

---

## ✨ Author  

**Kaustav Roy Chowdhury**  
💼 *Data Scientist | Machine Learning Enthusiast | SQL & Python*  
🔗 [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)  

> 💡 *"Don’t just query data — question it."*  
> 🌌 *"Every dataset tells a story waiting to be discovered."*  

---


## License & Acknowledgments

- Project is **Open Source**—free to use and build upon.
- Based on the Kaggle competition setup. Full details and dataset available on the competition page:contentReference[oaicite:7]{index=7}.
- Inspired by community contributions such as those by Sayak9 and team repositories. Special thanks to the Kaggle community for discussions and insights.

---

## Contact

Got feedback or collaboration ideas? Reach out to me via GitHub or email!

---

**Enjoy the cosmic detective work in machine learning—and may your predictions survive the voyage!**
::contentReference[oaicite:8]{index=8}
