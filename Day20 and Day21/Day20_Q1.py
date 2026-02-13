import pandas as pd
import numpy as np

# 1. Provided Data: List of Dictionaries
data = [
    {'Name': 'Alice', 'Score': 85},
    {'Name': 'Bob', 'Score': 70},
    {'Name': 'Charlie', 'Score': 95},
    {'Name': 'David', 'Score': 60},
    {'Name': 'Eve', 'Score': 80}
]

# 2. Convert to Pandas DataFrame
df = pd.DataFrame(data)

# 3. Use NumPy to calculate statistical measures
# Extract the Score column as a NumPy array for calculation
scores = df['Score'].values

mean_score = np.mean(scores)       #
median_score = np.median(scores)   #
std_dev = np.std(scores)           #

# 4. Add a conditional column
# Value is 'Above Average' if Score > Mean, otherwise 'Below Average'
df['Status'] = np.where(df['Score'] > mean_score, 'Above Average', 'Below Average')

# --- Output the Results ---
print("--- Resulting DataFrame ---")
print(df)
print("\n--- Summary Statistics ---")
print(f"Mean Score: {mean_score}")
print(f"Median Score: {median_score}")
print(f"Standard Deviation: {std_dev:.2f}")