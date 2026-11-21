import pandas as pd

# load dataset
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# count transactions
total = len(df)
fraud = len(df[df["Class"] == 1])
genuine = len(df[df["Class"] == 0])

# creating summary table
summary = pd.DataFrame({ # it will create a summary table
    "Category": ["Total Transactions", "Genuine Transactions", "Fraud Transactions"],
    "Count": [total, genuine, fraud]
})

print(summary)

# save summary table
summary.to_csv("dataset/fraud_summary.csv", index=False) # we use index= false because it avoids adding an extra index column.

# display summary
print("\nSummary saved successfully!")