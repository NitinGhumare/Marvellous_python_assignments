import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def FakeReal(data1, data2):
    # Step 1: Load and Combine
    df1 = pd.read_csv(data1)
    df2 = pd.read_csv(data2)

    df1['label'] = 0  # Fake
    df2['label'] = 1  # Real

    df = pd.concat([df1, df2], ignore_index=True)
    print("\n🔹 First 5 Rows of Combined Data:\n", df.head())
    print("\n🔹 Shape before column selection:", df.shape)

    # Step 2: Select required columns
    df = df[['text', 'label']]
    print("\n🔹 Null value count:\n", df.isna().sum())

    # Drop nulls
    df.dropna(inplace=True)
    print("\n🔹 Shape after dropping nulls:", df.shape)

    # Step 3: TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = tfidf.fit_transform(df['text'])
    y = df['label']

    print("\n🔹 TF-IDF Matrix Shape:", X.shape)
    print("\n🔹 Sample TF-IDF values from document 0:")
    sample_row = X[0]
    print(sample_row)

    # Step 4: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 5: Model Training
    lr = LogisticRegression()
    dt = DecisionTreeClassifier()

    lr.fit(X_train, y_train)
    dt.fit(X_train, y_train)

    # Step 6: Ensemble Voting Classifiers
    soft_vote = VotingClassifier(estimators=[('lr', lr), ('dt', dt)], voting='soft')
    hard_vote = VotingClassifier(estimators=[('lr', lr), ('dt', dt)], voting='hard')

    soft_vote.fit(X_train, y_train)
    hard_vote.fit(X_train, y_train)

    # Step 7: Evaluation
    models = {
        "Logistic Regression": lr,
        "Decision Tree": dt,
        "Soft Voting": soft_vote,
        "Hard Voting": hard_vote
    }

    for name, model in models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\n✅ {name} Accuracy: {acc:.4f}")
        print(f"📊 {name} Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print(f"📈 {name} Classification Report:\n", classification_report(y_test, y_pred))

def main():
    FakeReal("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()
