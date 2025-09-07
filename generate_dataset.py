import pandas as pd
import numpy as np

# Set random seed so results stay same
np.random.seed(42)

# Generate 200 fake students
data = {
    "attendance": np.random.randint(40, 100, 200),   # 40% - 100%
    "study_hours": np.random.randint(1, 20, 200),    # 1 - 20 hours per week
    "test_score": np.random.randint(30, 100, 200),   # 30 - 100 marks
}

df = pd.DataFrame(data)

# Define pass/fail rule (synthetic logic)
df["final_result"] = (
    (df["attendance"] > 60) &
    (df["study_hours"] > 5) &
    (df["test_score"] > 50)
).astype(int)

# Save to CSV
df.to_csv("student_data.csv", index=False)

print("✅ Fake dataset saved as student_data.csv")
print(df.head())
