import pandas as pd
import numpy as np

df = pd.read_csv('sales.csv')

df['Total'] = df['Quantity'] * df['Price']

total_sales = np.sum(df['Total'])
average_daily_sales = np.mean(df['Total'])
std_deviation_sales = np.std(df['Total'])

best_seller = df.groupby('Product')['Quantity'].sum().idxmax()

print(df)
print(f"Total Sales: {total_sales}")
print(f"Average Daily Sales: {average_daily_sales}")
print(f"Standard Deviation: {std_deviation_sales}")
print(f"Best Selling Product: {best_seller}")