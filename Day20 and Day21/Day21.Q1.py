import seaborn as sns
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 150, 120, 180, 200, 170]

sns.barplot(x=months, y=sales, hue=months, palette='viridis', legend=False)

plt.show()