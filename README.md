# 🔐 AI Password Security Analyzer

A machine learning-based password strength classifier that predicts whether a password is **Weak**, **Medium**, or **Strong** using character-level TF-IDF features and Multinomial Logistic Regression.

Unlike traditional password meters that rely only on predefined rules, this project learns password patterns from a large labeled dataset.

---

## 📌 Overview

The model performs **3-class password strength classification**:

| Label | Class |
|---|---|
| 0 | Weak |
| 1 | Medium |
| 2 | Strong |

The goal is to build an ML-based password analyzer capable of understanding character patterns and password complexity.

---

## 📂 Dataset

Dataset:

**Password Strength Classifier Dataset**  
https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset/data

The dataset contains:

- Password samples
- Strength labels (0, 1, 2)

After preprocessing, the dataset contains approximately:

```
670,000+ password samples
```
---

## 🧠 Machine Learning Approach

Pipeline:

```
Password
   ↓
Character Tokenization
   ↓
TF-IDF Vectorization
   ↓
Multinomial Logistic Regression
   ↓
Weak / Medium / Strong Prediction
```

Instead of analyzing passwords as complete words, the model learns from individual character patterns.

Example:

```
password123

↓
['p','a','s','s','w','o','r','d','1','2','3']
```

---

## ⚙️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib

---
## 📊 Performance

Test accuracy:

```
~84%
```

Classification performance:

```
              precision   recall   f1-score

Weak            0.47      0.85      0.61
Medium          0.96      0.81      0.88
Strong          0.91      0.97      0.94
```

---

Generated files:

```
password_model.pkl
vectorizer.pkl
```

## 👨‍💻 Author

**Nikoloz Chkhaidze**

Machine Learning / AI Project