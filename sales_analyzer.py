"""Sales Data Analyzer
A short project using Pandas and NumPy to analyse shop sales.
"""
import pandas as pd
import numpy as np

# Step 1: sales data
df = pd.DataFrame({
    "Product": ["Pen", "Book", "Bag", "Bottle", "Pencil"],
    "Price": [10, 120, 450, 80, 5],
    "Qty": [50, 20, 8, 15, 100]})

# Step 2: calculate revenue and sales status
df["Revenue"] = df["Price"] * df["Qty"]
df["Status"] = np.where(df["Revenue"] >= 1500, "High", "Low")

# Step 3: report
print(df)
print("Total Revenue:", df["Revenue"].sum())
best = df["Revenue"].idxmax()
print("Best Seller:", df.loc[best, "Product"])
