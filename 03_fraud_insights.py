import pandas as pd

df = pd.read_csv("dataset/cleaned_creditcard.csv")

# Fraud transactions
fraud = df[df["Class"] == 1]

# Genuine transactions
genuine = df[df["Class"] == 0]

# count transactions
print("Fraud Transactions:", len(fraud))
print("Genuine Transactions:", len(genuine))

# calculate fraud percentage
print("Fraud Percentage:", round((len(fraud) / len(df)) * 100, 2), "%")

# average fraud amount
print("Average Fraud Amount:", round(fraud["Amount"].mean(), 2))

# average genuine amount
print("Average Genuine Amount:", round(genuine["Amount"].mean(), 2))