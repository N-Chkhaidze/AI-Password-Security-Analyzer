import os
import pandas as pd
import joblib


# Configuration
INPUT_FILE = "14MIL-most-common.csv"
OUTPUT_FILE = "14MIL-labeled-passwords.csv"

MODEL_FILE = "password_model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"

BATCH_SIZE = 100000


def char_tokenizer(password):
    return list(password)


def load_model():
    print("Loading model...")

    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)

    return model, vectorizer


def label_passwords(model, vectorizer):

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    first_batch = True

    print("Starting labeling...")


    for batch_number, df in enumerate(
        pd.read_csv(
            INPUT_FILE,
            chunksize=BATCH_SIZE,
            on_bad_lines="skip"
        )
    ):

        print(f"Processing batch {batch_number + 1}")


        passwords = df["password"].astype(str)


        features = vectorizer.transform(passwords)


        predictions = model.predict(features)

        probabilities = model.predict_proba(features)

        confidence = probabilities.max(axis=1)


        labeled_data = pd.DataFrame({
            "password": passwords,
            "strength": predictions,
            "confidence": confidence
        })


        labeled_data.to_csv(
            OUTPUT_FILE,
            mode="a",
            header=first_batch,
            index=False
        )


        first_batch = False


    print("Labeling finished!")


def analyze_results():

    print("\nAnalyzing results...")


    df = pd.read_csv(
        OUTPUT_FILE
    )


    print("\nStrength distribution:")
    print(
        df["strength"].value_counts()
    )


    print("\nPercentage:")
    print(
        df["strength"]
        .value_counts(normalize=True)
        * 100
    )


    print("\nConfidence statistics:")
    print(
        df["confidence"].describe()
    )


    high_confidence = df[
        df["confidence"] > 0.99
    ]


    print(
        "\nHigh confidence predictions:",
        len(high_confidence)
    )


    high_confidence.to_csv(
        "high_confidence_passwords.csv",
        index=False
    )


if __name__ == "__main__":

    model, vectorizer = load_model()

    label_passwords(
        model,
        vectorizer
    )

    analyze_results()

    print("\nDone!")