# AI Password Security Analyzer

A machine learning-based password strength classifier that predicts whether a password is **Weak, Medium, or Strong** using **character-level TF-IDF features** and **Multinomial Logistic Regression**.

Unlike traditional password meters that rely only on predefined rules, this project learns password patterns from a large labeled dataset using machine learning.

---

# 📌 Overview

The model performs **3-class password strength classification**:

| Label | Class |
|------|------|
| 0 | Weak |
| 1 | Medium |
| 2 | Strong |

The goal is to build an ML-based password analyzer capable of understanding password structures and complexity patterns.

---

# 📂 Dataset

## Training Dataset

**Password Strength Classifier Dataset**

https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset/data

The dataset contains:

- Password samples
- Strength labels (0, 1, 2)

After preprocessing:

- ~670,000 labeled password samples were used for training

---

# 🧠 Machine Learning Approach

The complete pipeline:

```
Password
    ↓
Character-Level TF-IDF Vectorization
    ↓
Multinomial Logistic Regression
    ↓
Weak / Medium / Strong Prediction
```

Instead of manually creating features such as:

- Password length
- Number of digits
- Number of symbols
- Uppercase count

the model automatically learns important character patterns from passwords.

Example:

```
password123

↓

['p','a','s','s','w','o','r','d','1','2','3']
```

The TF-IDF representation allows the model to learn which character combinations are associated with weak or strong passwords.

---

# ⚙️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib

---

# 📊 Model Performance

Test accuracy:

```
~84%
```

Classification report:

```
              precision   recall   f1-score

Weak            0.47      0.85      0.61
Medium          0.96      0.81      0.88
Strong          0.91      0.97      0.94
```

Generated model files:

```
password_model.pkl
vectorizer.pkl
```

---

# 🚀 Large-Scale Password Labeling Extension

After training the classifier, the model was applied to a much larger password corpus to generate machine-learning-based labels.

## Dataset

**Common Password List (rockyou.txt)**

https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt

The dataset originates from the historical RockYou password leak and contains more than **14 million commonly used passwords**.

The original dataset contains passwords without strength labels.

---

# 🤖 Pseudo-Label Generation

The trained model was used to automatically classify each password.

For every password, the model generated:

- Predicted strength label
- Prediction confidence score

The labeling process was performed using batch processing to efficiently handle millions of passwords.

Example output:

| Password | Strength | Confidence |
|----------|----------|------------|
| 123456 | Weak | 99% |
| password123 | Medium | 85% |
| X7@k92Lm | Strong | 98% |

---

# 📈 14 Million Password Analysis Results

Total passwords analyzed:

```
14,316,879
```

Predicted distribution:

| Strength | Count | Percentage |
|----------|------:|-----------:|
| Weak (0) | 6,729,067 | 47.00% |
| Medium (1) | 6,782,947 | 47.38% |
| Strong (2) | 804,865 | 5.62% |

---

# 🎯 Prediction Confidence Analysis

Average model confidence:

```
82.4%
```

High-confidence predictions:

```
1,325,485 passwords
```

(Confidence > 99%)

This shows that a significant portion of predictions were classified with high certainty.

---

# 📁 Large-Scale Analysis Output

Generated files:

```
14MIL-labeled-passwords.csv
high_confidence_passwords.csv
```

Each labeled record contains:

- Password
- Predicted strength
- Confidence score


# 👨‍💻 Author

**Nikoloz Chkhaidze**

Machine Learning / AI Project