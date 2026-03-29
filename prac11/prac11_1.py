import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# a) Total profit of all months - Line Plot
plt.plot(df['month_number'], df['total_profit'], marker='o')
plt.title('Total Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Profit')
plt.show()

# b) All product sales - Multiline Plot
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in products:
    plt.plot(df['month_number'], df[product], label=product)
plt.legend()
plt.title('Product Sales Data')
plt.show()

# c) Face Cream vs Face Wash - Bar Chart
plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash')
plt.legend()
plt.title('Facial Product Sales')
plt.show()

# d) Total sale for last year - Pie Chart
total_sales = [df[p].sum() for p in products]
plt.pie(total_sales, labels=products, autopct='%1.1f%%')
plt.title('Yearly Sales Distribution by Product')
plt.show()