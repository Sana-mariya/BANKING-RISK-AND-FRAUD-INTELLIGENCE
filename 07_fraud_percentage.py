import pandas as pd

# load dataset
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# count total transactions
total = len(df)

# count fraud transactions
fraud = len(df[df["Class"] == 1])

# calculate fraud percentage
percentage = (fraud / total) * 100

# display results
print("Total Transactions:", total)
print("Fraud Transactions:", fraud)
print("Fraud Percentage:", round(percentage, 2), "%")