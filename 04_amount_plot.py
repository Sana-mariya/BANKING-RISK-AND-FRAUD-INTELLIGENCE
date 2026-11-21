import pandas as pd
import matplotlib.pyplot as plt # matplotlib used to create graphs and to visualise transaction amount

# load dastaset
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# seaprate fraud and genuine transactions
fraud = df[df["Class"] == 1]
genuine = df[df["Class"] == 0]

# creating box plot
plt.boxplot(   # compARE The transaction amount it will help to uunderstand median and spread of transaction amount.
    [genuine["Amount"], fraud["Amount"]],
    tick_labels=["Genuine", "Fraud"]
)

# adding title and labels 
plt.title("Fraud vs Genuine Transaction Amount")
plt.ylabel("Transaction Amount ($)")

# display chart
plt.show()
