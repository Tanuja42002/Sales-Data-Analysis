
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('ECOMM DATA.xlsx')

total_sales = df['Sales'].sum()

print('Total Sales:', total_sales)


#Plotting sales trends over time

plt.figure(figsize=(10,6))
sns.lineplot(data=monthly_sales)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Trends Over Time')
plt.show()


# Display top N best-selling products
N = 5
top_products = product_sales.head(N)
print('Top', N, 'Best-Selling Products:')
print(top_products)

# Bar chart for best-selling products
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Top Best-Selling Products')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show() 
