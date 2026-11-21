import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/creditcard.csv")

# Display first 5 rows
print(df.head())

# Check dataset information
print(df.info())

# Check dataset shape
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check fraud distribution
print("\nFraud Distribution:")
print(df["Class"].value_counts())

# Remove duplicate rows
df_clean = df.drop_duplicates()

# Check the new dataset size
print("\nOriginal Dataset:", df.shape)
print("Cleaned Dataset:", df_clean.shape)

# Save cleaned dataset
df_clean.to_csv("dataset/cleaned_creditcard.csv", index=False)

print("\nCleaned dataset saved successfully!")