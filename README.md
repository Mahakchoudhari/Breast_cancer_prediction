# Breast Cancer Prediction using Logistic Regression

##  Overview

This project predicts whether a tumor is **benign** or **malignant** using Logistic Regression based on medical cell features.

##  Objective

To build a machine learning model that helps classify breast cancer cases for early detection.

## Dataset

The dataset consists of several cell-related features:

* Sample Code Number
* Clump Thickness
* Uniformity of Cell Size
* Uniformity of Cell Shape
* Marginal Adhesion
* Single Epithelial Cell Size
* Bare Nuclei
* Bland Chromatin
* Normal Nucleoli
* Mitoses

###  Target Variable

* `2` → Benign (Non-cancerous)
* `4` → Malignant (Cancerous)

##  Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Jupyter

## Model Used

* Logistic Regression

## 🔄 Workflow

1. Data loading and cleaning
2. Feature scaling
3. Splitting dataset into training and testing sets
4. Training Logistic Regression model
5. Prediction and evaluation

## Example Input

```
Clump Thickness: 5  
Uniformity of Cell Size: 1  
Uniformity of Cell Shape: 1  
Marginal Adhesion: 1  
Single Epithelial Cell Size: 2  
Bare Nuclei: 1  
Bland Chromatin: 3  
Normal Nucleoli: 1  
Mitoses: 1  
```

###  Prediction Output

The model will classify the tumor as either:

* `2` (Benign) or
* `4` (Malignant)

##  Evaluation Metrics

* Confusion Matrix
* Accuracy Score

## Future Improvements

* Use advanced models like Random Forest or SVM
* Perform feature selection
* Hyperparameter tuning

##  Conclusion

This project demonstrates how Logistic Regression can be used in healthcare to classify tumors and support early breast cancer diagnosis.

---

*Simple yet powerful classification model for real-world healthcare problems.*
