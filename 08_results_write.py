import pandas as pd

# load dataset
df = pd.read_csv("dataset/cleaned_creditcard.csv")

# counting transactions
total = len(df)
fraud = len(df[df["Class"] == 1])
genuine = len(df[df["Class"] == 0])

# calculate fraud percentage
percentage = (fraud / total) * 100

# create result file
file = open("results.txt", "w") # w means write mode

# write project results
file.write("BANKING FRAUD ANALYTICS PROJECT\n") #\n used to moves the  next results to a new line
file.write("--------------------------------\n")
file.write(f"Total Transactions: {total}\n")
file.write(f"Genuine Transactions: {genuine}\n")
file.write(f"Fraud Transactions: {fraud}\n")
file.write(f"Fraud Percentage: {percentage:.2f}%\n")

# close file
file.close()

print("Results saved successfully!")