import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import joblib



df = pd.read_csv(
    "data.csv",
    on_bad_lines="skip"
)


passwords = df["password"].astype(str)

labels = df["strength"]



def char_tokenizer(password):

    return list(password)



vectorizer = TfidfVectorizer(
    tokenizer=char_tokenizer,
    token_pattern=None,
    lowercase=False,
    min_df=2,
    sublinear_tf=True
)


X = vectorizer.fit_transform(passwords)



X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)



model = LogisticRegression(
    multi_class="multinomial",
    max_iter=1000,
    class_weight="balanced"
)


model.fit(
    X_train,
    y_train
)



pred = model.predict(X_test)



print(
    classification_report(
        y_test,
        pred
    )
)



joblib.dump(
    model,
    "password_model.pkl"
)


joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)