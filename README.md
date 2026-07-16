## Large-Scale Analysis Dataset (14M Passwords)

For large-scale password security analysis, the trained AI model was applied to a dataset containing **14+ million commonly used passwords**.

### Dataset Source

Kaggle:
https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt

The dataset is based on the **RockYou password list**, a widely used cybersecurity research dataset originating from the 2009 RockYou data breach.

It is commonly used for:
- Password security research
- Password pattern analysis
- Machine learning experiments in cybersecurity

## Labeling Process

The original dataset does not contain password strength labels. Therefore, the trained machine learning model was used to automatically generate strength classifications.

Pipeline:

14M Password Dataset
        ↓
Trained TF-IDF + Logistic Regression Model
        ↓
Predicted Strength Labels
        ↓
Confidence Score Analysis

Generated labels:

0 → Weak  
1 → Medium  
2 → Strong  

For each password, the model generated:

- Predicted strength category
- Prediction confidence score

Example:

| Password | Strength | Confidence |
|----------|----------|------------|
| 123456 | Weak | 99% |
| password123 | Medium | 87% |
| X7@k92Lm | Strong | 97% |

## Analysis Results

The model analyzed **14.3 million password samples**.

### Strength Distribution

| Category | Number of Passwords | Percentage |
|----------|---------------------|------------|
| Weak (0) | 6,729,067 | 47.00% |
| Medium (1) | 6,782,947 | 47.38% |
| Strong (2) | 804,865 | 5.62% |

### Prediction Confidence

Average confidence:

82.39%

Median confidence:

86.39%

High-confidence predictions:

1,325,485 passwords

with confidence above:

99%

## Output Dataset

The generated labeled dataset contains:

- password
- strength
- confidence
