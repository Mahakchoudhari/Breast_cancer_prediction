# 🎗️ Breast Cancer Prediction

A Machine Learning web application that predicts whether a tumor is **Benign or Malignant** based on patient data.

---

## 📌 Project Overview

Breast cancer is one of the most common cancers worldwide. Early detection can significantly improve survival rates. This project uses Machine Learning classification algorithms to predict breast cancer based on tumor characteristics.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Deployment:** Streamlit

---

## 📊 Dataset

- **Name:** Breast Cancer Wisconsin Dataset
- **Source:** UCI Machine Learning Repository
- **Samples:** 699
- **Features:** 9 (Clump Thickness, Uniformity of Cell Size, Uniformity of Cell Shape, etc.)
- **Target:** Class (2 = Benign, 4 = Malignant)

---

## 🔍 Project Structure

```
Breast_cancer_prediction/
│
├── breast_cancer.csv        ← Dataset
├── breast_cancer.ipynb      ← Jupyter Notebook
├── app.py                   ← Streamlit App
├── model.pkl                ← Saved Model
├── scaler.pkl               ← Saved Scaler
├── requirements.txt         ← Requirements  
└── README.md

```

---

## 📈 Steps Followed

1. **Data Preprocessing** — Removed unnecessary columns, handled missing values
2. **EDA & Visualizations** — Countplot, Correlation Heatmap, Feature Distribution Histplot , Boxplot
3. **Train Test Split** — 80/20 split
4. **Feature Scaling** — StandardScaler
5. **Model Training** — Random Forest Classification
6. **Evaluation** — Confusion Matrix, Accuracy Score, Cross Validation
7. **Model Comparison** — Logistic Regression, Random Forest, SVM, KNN, Decision Tree
8. **Deployment** — Streamlit Web App

---

## ✅ Model Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | 97.08% |
| Cross Validation Accuracy | 96.70% |
| Standard Deviation | 2.58% |

---

## 🤖 Models Compared

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 95.62% |
| Random Forest | 97.08% |
| SVM | 95.62% |
| KNN | 95.62% |
| Decision Tree | 94.16% |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Mahakchoudhari/Breast_cancer_prediction.git
cd Breast_cancer_prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run Streamlit App**
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
```

---

## 👩‍💻 Author

**Mahak Choudhari**  
B.Tech — Artificial Intelligence & Machine Learning (2nd Year)  
[GitHub](https://github.com/Mahakchoudhari)

