import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

# Project 7: Loan Approval Prediction

# 1. Load dataset
loans = pd.read_csv("loan_approval.csv")

# 2. Inspect dataset
print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(loans.head())

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(loans.shape)

print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(loans.columns)

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)
loans.info()

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(loans.describe())

# 3. Data quality
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(loans.isnull().sum())

print("\n" + "=" * 50)
print("DUPLICATES")
print("=" * 50)
print("Number of duplicate rows:", loans.duplicated().sum())

print("\n" + "=" * 50)
print("LOAN APPROVAL DISTRIBUTION")
print("=" * 50)
print(loans["Loan_Approved"].value_counts())

# 4. Feature engineering
loans["Loan_to_Income"] = loans["Loan_Amount"] / loans["Income"]

print("\n" + "=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50)
print(loans[["Income", "Loan_Amount", "Loan_to_Income"]].head(10))

# 5. Features and target
feature_columns = [
    "Income",
    "Credit_Score",
    "Loan_Amount",
    "Employment_Years",
    "Age",
    "Existing_Loan",
    "Loan_to_Income",
]

X = loans[feature_columns]
y = loans["Loan_Approved"]

print("\n" + "=" * 50)
print("FEATURES (X)")
print("=" * 50)
print(X.head())

print("\n" + "=" * 50)
print("TARGET (y)")
print("=" * 50)
print(y.head())
print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)

# 6. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print("\n" + "=" * 50)
print("TRAIN / TEST SPLIT")
print("=" * 50)
print("Training features:", X_train.shape)
print("Testing features :", X_test.shape)
print("Training target  :", y_train.shape)
print("Testing target   :", y_test.shape)

print("\nTraining approval distribution:")
print(y_train.value_counts())
print("\nTesting approval distribution:")
print(y_test.value_counts())

# 7. Feature scaling for Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n" + "=" * 50)
print("FEATURE SCALING")
print("=" * 50)
print("Original training data:")
print(X_train.head())
print("\nScaled training data:")
print(X_train_scaled[:5])

# 8. Logistic Regression
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

print("\n" + "=" * 50)
print("LOGISTIC REGRESSION")
print("=" * 50)
print("Model training completed successfully!")

# 9. Logistic Regression predictions
y_pred = model.predict(X_test_scaled)

print("\n" + "=" * 50)
print("LOGISTIC REGRESSION PREDICTIONS")
print("=" * 50)
print("Actual values    :", y_test.values)
print("Predicted values :", y_pred)

# 10. Logistic Regression evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n" + "=" * 50)
print("LOGISTIC REGRESSION EVALUATION")
print("=" * 50)
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall   : {recall:.2f}")
print(f"F1 Score : {f1:.2f}")

# 11. Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\n" + "=" * 50)
print("CONFUSION MATRIX")
print("=" * 50)
print(cm)

# 12. Logistic Regression ROC-AUC
y_prob = model.predict_proba(X_test_scaled)[:, 1]
roc_auc = roc_auc_score(y_test, y_prob)

print("\n" + "=" * 50)
print("LOGISTIC REGRESSION ROC-AUC")
print("=" * 50)
print("Approval probabilities:", y_prob)
print(f"ROC-AUC Score: {roc_auc:.2f}")

# 13. Threshold experiment
threshold = 0.60
y_pred_threshold = (y_prob >= threshold).astype(int)

print("\n" + "=" * 50)
print("THRESHOLD EXPERIMENT")
print("=" * 50)
print("Threshold:", threshold)
print("Predictions:", y_pred_threshold)
print("\nOriginal predictions:")
print(y_pred)

# 14. Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("\n" + "=" * 50)
print("RANDOM FOREST")
print("=" * 50)
print("Random Forest training completed!")
print("\nActual values    :", y_test.values)
print("Predicted values :", rf_pred)

# 15. Random Forest evaluation
rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)

print("\n" + "=" * 50)
print("RANDOM FOREST EVALUATION")
print("=" * 50)
print(f"Accuracy : {rf_accuracy:.2f}")
print(f"Precision: {rf_precision:.2f}")
print(f"Recall   : {rf_recall:.2f}")
print(f"F1 Score : {rf_f1:.2f}")

# 16. Random Forest ROC-AUC
rf_prob = rf_model.predict_proba(X_test)[:, 1]
rf_roc_auc = roc_auc_score(y_test, rf_prob)

print("\n" + "=" * 50)
print("RANDOM FOREST ROC-AUC")
print("=" * 50)
print("Approval probabilities:", rf_prob)
print(f"ROC-AUC Score: {rf_roc_auc:.2f}")

# 17. Model comparison
comparison = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"],
    "Logistic Regression": [accuracy, precision, recall, f1, roc_auc],
    "Random Forest": [rf_accuracy, rf_precision, rf_recall, rf_f1, rf_roc_auc],
})

print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)
print(comparison.round(2))

# 18. New applicant prediction
new_applicant = pd.DataFrame({
    "Income": [70000],
    "Credit_Score": [760],
    "Loan_Amount": [400000],
    "Employment_Years": [7],
    "Age": [35],
    "Existing_Loan": [0],
    "Loan_to_Income": [400000 / 70000],
})

print("\n" + "=" * 50)
print("NEW APPLICANT")
print("=" * 50)
print(new_applicant)

new_applicant_scaled = scaler.transform(new_applicant)

lr_prediction = model.predict(new_applicant_scaled)[0]
lr_probability = model.predict_proba(new_applicant_scaled)[0][1]

rf_prediction = rf_model.predict(new_applicant)[0]
rf_probability = rf_model.predict_proba(new_applicant)[0][1]

print("\n" + "=" * 50)
print("NEW APPLICANT PREDICTION")
print("=" * 50)
print("Logistic Regression:", "Approved" if lr_prediction == 1 else "Rejected")
print(f"Logistic Regression approval probability: {lr_probability:.2%}")
print("Random Forest:", "Approved" if rf_prediction == 1 else "Rejected")
print(f"Random Forest approval probability: {rf_probability:.2%}")

# 19. Random Forest feature importance
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_,
}).sort_values(by="Importance", ascending=False)

print("\n" + "=" * 50)
print("RANDOM FOREST FEATURE IMPORTANCE")
print("=" * 50)
print(feature_importance)
