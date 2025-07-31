import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
import matplotlib.pyplot as plt
import seaborn as sns

def BankStatus(datapath):
    df = pd.read_csv(datapath, sep=";") 
    print(df.isna().sum())
    print("Statistics of data is:\n", df.describe()) 
    
    df = df.drop(columns=["contact", "poutcome"])

    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop(columns=['y'])
    Y = df['y']

    scaler = StandardScaler() 
    X_scaled = scaler.fit_transform(X) 

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    # Define models
    log_clf = LogisticRegression()
    knn = KNeighborsClassifier(n_neighbors=5)
    rf = RandomForestClassifier(n_estimators=150, random_state=42) 

    # Train individually
    log_clf.fit(X_train, Y_train)
    knn.fit(X_train, Y_train)
    rf.fit(X_train, Y_train)

    # Predictions
    y_log_pred = log_clf.predict(X_test)
    y_knn_pred = knn.predict(X_test)
    y_rf_pred = rf.predict(X_test)

    # Probabilities
    log_proba = log_clf.predict_proba(X_test)[:,1]
    knn_proba = knn.predict_proba(X_test)[:,1]
    rf_proba = rf.predict_proba(X_test)[:,1]

    # ROC-AUC
    log_auc = roc_auc_score(Y_test, log_proba)
    knn_auc = roc_auc_score(Y_test, knn_proba)
    rf_auc = roc_auc_score(Y_test, rf_proba)

    # Accuracy
    log_acc = accuracy_score(Y_test, y_log_pred)
    knn_acc = accuracy_score(Y_test, y_knn_pred)
    rf_acc = accuracy_score(Y_test, y_rf_pred)

    # Print comparison
    print("\n--- Model Comparison ---")
    print(f"Logistic Regression:\tAccuracy = {log_acc:.4f}, ROC AUC = {log_auc:.4f}")
    print(f"K-Nearest Neighbors:\tAccuracy = {knn_acc:.4f}, ROC AUC = {knn_auc:.4f}")
    print(f"Random Forest:\t\tAccuracy = {rf_acc:.4f}, ROC AUC = {rf_auc:.4f}")

    # ROC Plot
    RocCurveDisplay.from_estimator(log_clf, X_test, Y_test, name="Logistic")
    RocCurveDisplay.from_estimator(knn, X_test, Y_test, name="KNN")
    RocCurveDisplay.from_estimator(rf, X_test, Y_test, name="Random Forest")
    plt.title("ROC Curve Comparison")
    plt.legend()
    plt.show()

    # Voting Classifier
    voting_clf = VotingClassifier(estimators=[
        ("lr", log_clf),
        ("knn", knn),
        ("rf", rf)
    ], voting="soft")

    voting_clf.fit(X_train, Y_train)
    Y_pred = voting_clf.predict(X_test)

    print("\n--- Voting Classifier ---")
    print("Accuracy:", accuracy_score(Y_test, Y_pred))
    CM = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix:\n", CM)
    print("Classification Report:\n", classification_report(Y_test, Y_pred))

    vote_proba = voting_clf.predict_proba(X_test)[:,1]
    print("ROC AUC Score:", roc_auc_score(Y_test, vote_proba))

    # Confusion matrix heatmap
    sns.heatmap(CM, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Voting Classifier")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # ROC for Voting Classifier
    RocCurveDisplay.from_estimator(voting_clf, X_test, Y_test, name="Voting Classifier")
    plt.title("ROC Curve - Voting Classifier")
    plt.show()

def main():
    BankStatus("bank-full.csv")

if __name__ == "__main__":
    main()
