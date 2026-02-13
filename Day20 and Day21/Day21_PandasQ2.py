import pandas as pd

# 'header=1' tells pandas that the real column names are in the second row
df = pd.read_excel('sales_data.xlsx', sheet_name='2025', header=1)

# Now it will find 'Quantity' and 'Price' perfectly
df['Total'] = df['Quantity'] * df['Price']

df.to_excel('sales_summary.xlsx', index=False)