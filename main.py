import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("attendance.csv")

print("Data loaded successfully\n")
print(data.head())

X = data.drop("At_Risk", axis=1)
y = data["At_Risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nModel Evaluation")
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

new_student = pd.DataFrame([{
    "Avg_Login_Time": 30,
    "Missed_Classes": 6,
    "Assignment_Rate": 55,
    "Internet_Issue": 1,
    "Participation": 4
}])

new_student = new_student[X.columns]

result = model.predict(new_student)

print("\nNew Student Prediction")
print("Student is AT RISK of low attendance" if result[0] == 1 else "Student is NOT at risk")
