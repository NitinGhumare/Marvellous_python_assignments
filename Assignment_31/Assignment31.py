import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def BrestCancer(datapath):
    df = pd.read_csv(datapath) 

    df = df.drop(columns=['CodeNumber'])
    df['BareNuclei'] = df['BareNuclei'].replace('?', np.nan)
    df = df.dropna(subset=['BareNuclei'])
    df['BareNuclei'] = df['BareNuclei'].astype(int)
    df['CancerType'] = df['CancerType'].map({2: 0, 4: 1})

    X = df.drop(columns=['CancerType']) 
    Y = df['CancerType'] 

    scaler = StandardScaler() 
    X_scaled = scaler.fit_transform(X) 

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    ### --- Single Decision Tree ---
    print("\n===== Single Decision Tree =====")
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, Y_train)
    Y_pred_dt = dt.predict(X_test)

    print("Accuracy:", accuracy_score(Y_test, Y_pred_dt))
    print("Classification Report:\n", classification_report(Y_test, Y_pred_dt))
    print("ROC-AUC Score:", roc_auc_score(Y_test, Y_pred_dt))

    cm_dt = confusion_matrix(Y_test, Y_pred_dt)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Decision Tree")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

    ### --- Ensemble: Random Forest + Gradient Boosting ---
    print("\n===== Ensemble: RF + GB =====")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)

    ensemble = VotingClassifier(estimators=[
        ("RF", rf),
        ("GB", gb)
    ], voting="soft")

    ensemble.fit(X_train, Y_train)
    Y_pred_ens = ensemble.predict(X_test)

    print("Accuracy:", accuracy_score(Y_test, Y_pred_ens))
    print("Classification Report:\n", classification_report(Y_test, Y_pred_ens))
    print("ROC-AUC Score:", roc_auc_score(Y_test, Y_pred_ens))

    cm_ens = confusion_matrix(Y_test, Y_pred_ens)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_ens, annot=True, fmt='d', cmap='Greens')
    plt.title("Confusion Matrix - Ensemble (RF + GB)")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

    ### --- ROC Curve Comparison ---
    y_proba_dt = dt.predict_proba(X_test)[:, 1]
    y_proba_ens = ensemble.predict_proba(X_test)[:, 1]
    fpr_dt, tpr_dt, _ = roc_curve(Y_test, y_proba_dt)
    fpr_ens, tpr_ens, _ = roc_curve(Y_test, y_proba_ens)

    plt.figure(figsize=(7, 5))
    plt.plot(fpr_dt, tpr_dt, label=f"Decision Tree (AUC = {roc_auc_score(Y_test, y_proba_dt):.2f})", color='blue')
    plt.plot(fpr_ens, tpr_ens, label=f"RF + GB Ensemble (AUC = {roc_auc_score(Y_test, y_proba_ens):.2f})", color='green')
    plt.plot([0, 1], [0, 1], 'k--', lw=1)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()

    ### --- Feature Importance (Random Forest & GB) ---
    print("\nFeature Importance from Random Forest:")
    rf.fit(X_train, Y_train)
    importance_rf = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
    importance_rf.plot(kind='bar', figsize=(10,6), title="Feature Importance - Random Forest")
    plt.ylabel("Importance Score")
    plt.tight_layout()
    plt.show()

    print("\nFeature Importance from Gradient Boosting:")
    gb.fit(X_train, Y_train)
    importance_gb = pd.Series(gb.feature_importances_, index=X.columns).sort_values(ascending=False)
    importance_gb.plot(kind='bar', figsize=(10,6), title="Feature Importance - Gradient Boosting")
    plt.ylabel("Importance Score")
    plt.tight_layout()
    plt.show()

def main():
    BrestCancer("breast-cancer-wisconsin.csv")

if __name__=="__main__":
    main()
