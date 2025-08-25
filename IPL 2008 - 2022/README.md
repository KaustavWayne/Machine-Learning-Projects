# 🏏 IPL Batsman Segmentation using K-Means Clustering

Segment IPL batsmen into meaningful groups (e.g., power-hitters, anchors, finishers) using K-Means on performance features engineered from ball-by-ball data.

> “In God we trust; all others must bring data.” — W. Edwards Deming

[Dataset (Kaggle): IPL 2008–2021 All Match Dataset](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset)

---

## Overview

This project clusters IPL batsmen based on performance profiles derived from ball-by-ball data. The goal is to uncover roles and styles—such as powerplay aggressors, middle-over anchors, and death-overs finishers—purely from data.

Key ideas:
- Engineer robust, interpretable batting features
- Scale features and select K via elbow and silhouette
- Train K-Means and label segments with human-friendly names
- Visualize clusters and profile centroids for interpretation

> “Simplicity is prerequisite for reliability.” — Edsger W. Dijkstra

---

## Quickstart

1) Clone and set up environment
```bash
git clone https://github.com/your-org/ipl-batsman-kmeans.git
cd ipl-batsman-kmeans
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2) Download data from Kaggle
- Create Kaggle API token (Account → API → Create New Token)
- Place kaggle.json in ~/.kaggle/ (Linux/Mac) or %USERPROFILE%\.kaggle\ (Windows)
```bash
mkdir -p data/raw
kaggle datasets download -d vora1011/ipl-2008-to-2021-all-match-dataset -p data/raw
unzip data/raw/ipl-2008-to-2021-all-match-dataset.zip -d data/raw
```

3) Run the pipeline
```bash
python src/segment_batsmen.py \
  --raw_dir data/raw \
  --out_csv data/processed/batsman_segments.csv \
  --min_balls 150 \
  --k auto
```

> “Make it work, make it right, make it fast.” — Kent Beck

---

## Project Structure

```
.
├── data/
│   ├── raw/              # Kaggle CSVs
│   └── processed/        # Engineered features, cluster outputs
├── notebooks/
│   ├── 01_feature_engineering.ipynb
│   └── 02_clustering_and_viz.ipynb
├── src/
│   ├── features.py       # Feature engineering
│   ├── clustering.py     # K selection, KMeans training
│   ├── viz.py            # PCA/UMAP, radar charts
│   └── segment_batsmen.py
├── requirements.txt
└── README.md
```

---

## Dataset

- IPL 2008–2021: [Kaggle](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset)
- Check the dataset page for terms, schema, and file names. Typical files include matches-level and ball-by-ball deliveries.

> “Programs must be written for people to read, and only incidentally for machines to execute.” — Harold Abelson & Gerald Jay Sussman

---

## Feature Engineering

We compute season-agnostic, role-revealing features at the batsman level. Commonly derivable (from ball-by-ball):

- Volume and scoring
  - Balls faced
  - Runs
  - Strike Rate (SR) = 100 × runs / balls_faced
  - Batting Average (AVG) ≈ runs / dismissals (guard against div-by-zero)
- Shot profile
  - 4s, 6s, Boundary% = 100 × (4s + 6s) / balls_faced
  - Dot% = 100 × dot_balls / balls_faced
- Phase split (if over number is available)
  - PP SR (overs 1–6), Middle SR (7–15), Death SR (16–20)
- Consistency (if match_id and inning are available)
  - 30+%, 50+% per innings
- Optional robustness
  - Log/Box-Cox transforms for skewed features
  - Min sample filter: e.g., min_balls ≥ 150

> “Premature optimization is the root of all evil.” — Donald Knuth

---

## Modeling

- Scale features (StandardScaler or RobustScaler)
- Choose K using elbow (inertia) and silhouette
- Fit KMeans (random_state=42, n_init=10)
- Label segments heuristically (based on centroid profiles), e.g.:
  - Power-Hitters (high SR, high Boundary%, high Death SR)
  - Anchors (high AVG, lower Boundary%, solid Middle SR)
  - Finishers (elevated Death SR, good SR on low balls faced)
  - All-Round Stabilizers (balanced metrics, low dot%)
  - Emerging/Low-Volume (below sample threshold, if retained)

> “All models are wrong, but some are useful.” — George E. P. Box

---

## Acknowledgements

- Dataset curators: [vora1011](https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset)
- Community inspiration from sports analytics and open-source data science

> “The most powerful tool we have as developers is automation.” — Scott Hanselman

---
