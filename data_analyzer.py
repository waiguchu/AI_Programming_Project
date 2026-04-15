import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataseet
df = pd.read_csv("employees.csv")

# Inspect dataset
print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

# Clean data
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Simple statistics
print("\nDiscriptive statistics:")
print(df.describe())

# Visualization
plt.bar(df['numeric_column'], bins=20, color='skyblue', edgecolor='black')
plt.title("Scatter Plot of X vs Y")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show
