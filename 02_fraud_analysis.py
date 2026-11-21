import pandas as pd
# load vlean data
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# total transactions
print("Total Transactions:", len(df)) #len used for to calculate total transaction len(count)

# fraud and genuine transactions
print("\nFraud and Genuine Transactions:")
print(df["Class"].value_counts())

# average transaction amount
print("\nAverage Transaction Amount:")
print(round(df["Amount"].mean(), 2))   # round used because i don't want complicated decimals i want result simple. used 2 for only 2 decimals.
