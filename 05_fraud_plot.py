import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# count transactions
count = df["Class"].value_counts()  # value count used to count fraud and genuine transactions

# creating bar chart
plt.bar(["Genuine", "Fraud"], [count[0], count[1]])

# use log scale
plt.yscale("log") # log used because we have very large transactions so i took log to show large diffrences in counts clearly

# adding chart title and labels
plt.title("Fraud vs Genuine Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Transactions (Log Scale)")

# display chart
plt.show()