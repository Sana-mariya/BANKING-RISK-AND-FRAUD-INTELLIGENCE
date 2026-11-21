import pandas as pd
from pathlib import Path

# Find the dataset
folder = Path(__file__).resolve().parent.parent
files = list(folder.rglob("*.csv"))

data_file = None

for file in files:
    if "cleaned" in file.name.lower() and "credit" in file.name.lower():
        data_file = file
        break

if data_file is None:
    print("Dataset not found")

else:
    df = pd.read_csv(data_file)

    print("FEATURE ANALYSIS")

    # Find correlation with fraud
    correlation = df.corr(numeric_only=True)["Class"] # correlation tells us whether two numerical variables move together and how strogly they are realted

    print("\nFeature Correlation with Fraud:")
    print(correlation.drop("Class").abs().sort_values(ascending=False).head(10))

    # Save results
    correlation.to_csv("feature_correlation.csv")

    print("\nFeature Analysis Completed!")

    # Average Transaction Amount Comparison

print("\nAverage Transaction Amount")

normal = df[df["Class"] == 0]
fraud = df[df["Class"] == 1]

print("Normal Transaction Average:")
print(normal["Amount"].mean())

print("Fraud Transaction Average:")
print(fraud["Amount"].mean())

print("\nAnalysis Completed!")

# Transaction Amount Range Analysis

print("\nTransaction Amount Range Analysis")

df["Amount Range"] = pd.cut(
    df["Amount"],
    bins=[-1, 100, 500, float("inf")],
    labels=["Low", "Medium", "High"]
)

print("\nTransaction Count by Amount Range:")
print(df["Amount Range"].value_counts())

print("\nFraud Count by Amount Range:")
print(pd.crosstab(df["Amount Range"], df["Class"]))

print("\nAnalysis Completed!")