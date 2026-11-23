
# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 2. Load the customer churn dataset
df = pd.read_csv("customer_churn.csv")

# 3. Display dataset details
print("First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)

# 4. Descriptive Statistics
num = df.select_dtypes(include='number')

print("\nMean:")
print(num.mean())

print("\nMedian:")
print(num.median())

print("\nMode:")
print(df.mode().iloc[0])

print("\nStandard Deviation:")
print(num.std())

print("\nVariance:")
print(num.var())

print("\nMinimum Values:")
print(num.min())

print("\nMaximum Values:")
print(num.max())

print("\nPercentiles:")
print(num.quantile([0.25, 0.50, 0.75]))

print("\nDescriptive Statistics:")
print(df.describe())

# 5. Data Visualization

# Histogram
num.hist(figsize=(10, 8))
plt.show()

# Box Plot
plt.figure(figsize=(10, 5))
sns.boxplot(data=num)
plt.show()

# Scatter Plot
if len(num.columns) >= 2:
    sns.scatterplot(x=num.columns[0], y=num.columns[1], data=df)
    plt.show()

# Correlation Matrix
corr = num.corr()

# Heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 6. Handle Missing Data
print("\nMissing Values:")
print(df.isnull().sum())

# Replace missing numerical values with mean
df[num.columns] = df[num.columns].fillna(num.mean())

# Remove rows containing remaining missing values
df.dropna(inplace=True)

print("\nCleaned Dataset:")
print(df.head())

# 7. Detect and Handle Outliers

# Calculate Z-scores for numerical columns
num = df.select_dtypes(include='number')

z_scores = num.apply(zscore)

# Identify outliers
outliers = (z_scores.abs() > 3)

print("\nDetected Outliers:")
print(df[outliers.any(axis=1)])

# Remove records containing outliers
df = df[~outliers.any(axis=1)]

# 8. Verify Cleaned Dataset
print("\nRemaining Missing Values:")
print(df.isnull().sum())

# Check remaining outliers
num = df.select_dtypes(include='number')
z_scores = num.apply(zscore)

print("\nRemaining Outliers:")
print((z_scores.abs() > 3).sum())

print("\nFinal Dataset:")
print(df)

# 9. Save Cleaned Dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")
