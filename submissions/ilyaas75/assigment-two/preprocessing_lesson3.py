
# Lesson 3 Preprocessing Script
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("student_study_habits_dataset.csv")

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Separate features and label
X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled feature sample:")
print(X_scaled[:5])
