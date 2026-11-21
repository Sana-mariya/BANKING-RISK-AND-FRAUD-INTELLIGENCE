import pandas as pd
from pathlib import Path

# Find the project folder
folder = Path(__file__).resolve().parent.parent

# Find the cleaned dataset
files = list(folder.rglob("*.csv"))

for file in files:
    name = file.name.lower()

    if "cleaned" in name and "credit" in name and "card" in name:
        df = pd.read_csv(file)
        print("Dataset Loaded Successfully!")
        break

# Fraud Pattern Analysis

print("\nFRAUD PATTERN ANALYSIS")

# 1. Count transactions
print("\nTransaction Count:")
print(df["Class"].value_counts())

# 2. Find fraud transactions
fraud = df[df["Class"] == 1]

print("\nTotal Fraud Transactions:")
print(len(fraud))

# 3. Calculate fraud percentage
percentage = (len(fraud) / len(df)) * 100

print("\nFraud Percentage:")
print(round(percentage, 2), "%")

# 4. Average fraud amount
print("\nAverage Fraud Amount:")
print(fraud["Amount"].mean())

# 5. Highest fraud amount
print("\nHighest Fraud Amount:")
print(fraud["Amount"].max())

# 6. Lowest fraud amount
print("\nLowest Fraud Amount:")
print(fraud["Amount"].min())

# 7. Save fraud transactions
output_folder = Path(__file__).resolve().parent / "Results"
output_folder.mkdir(exist_ok=True) # mkdir used to create a folder

fraud.to_csv(output_folder / "fraud_transactions.csv", index=False)

print("\nFraud Pattern Analysis Completed!")
print("Results saved successfully!")