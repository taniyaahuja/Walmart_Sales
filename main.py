import numpy as np               #linear algebra
import pandas as pd              #data processing
import matplotlib.pyplot as plt  #data visualisation
import seaborn as sns

filename = (r'C:\Users\taniy\Downloads\Walmart Sales.xlsx')

xls = pd.ExcelFile(filename)     #importing our data
print (xls.sheet_names)          #printing sheet names

df = xls.parse('Sheet1')
print(df)                        #printing data from excel file

print(df.info())                 #basic information about the dataset
print(df.isnull().sum())         #checking for null values
print(df.describe())             #statistical description of the dataset

## A. Analyze the performance of sales and revenue at the city and branch level

#Creating revenue column
df['Revenue'] = df['Unit price'] * df['Quantity']

# Group by City to calculate total revenue and sales for each branch
city_perf = df.groupby('City').agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()

#Group by Branch to calculate total revenue and sales for each branch
branch_perf = df.groupby('Branch').agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()

print("Revenue and Sales by city:")
print(city_perf)

print("Revenue and Sales by branch:")
print(branch_perf)

#Group by City and Branch to calculate sales and revenue for each branch in each city
sales_rev_by_city_branch = df.groupby(['City', 'Branch']).agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()

print("\nTotal Revenue and Sales by Branch in Each City:")
print(sales_rev_by_city_branch)

#Total Revenue of each branch in each city
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Revenue', hue='Branch', data=sales_rev_by_city_branch, palette="Blues")
plt.title('Total Revenue by Branch in Each City')
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.legend(title='Branch')
plt.show()

#Total Sales (quantity) by city and branch
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Quantity', hue='Branch', data=sales_rev_by_city_branch, palette="YlOrBr")
plt.title('Total Quantity Sold by Branch in Each City')
plt.xlabel('City')
plt.ylabel('Total Quantity Sold')
plt.legend(title='Branch')
plt.show()

## B. What is the average price of an item sold at each branch of the city

avg_price_by_city_branch = df.groupby(["City", "Branch"])["Unit price"].mean().reset_index()
print(avg_price_by_city_branch)

plt.figure(figsize=(8, 6))
sns.barplot(x="City", y="Unit price", hue="Branch", data=avg_price_by_city_branch, palette="viridis")
plt.title("Average Unit Price by City and Branch")
plt.xlabel("City")
plt.ylabel("Average Unit Price")
plt.show()

## C. Analyze the performance of sales and revenue, Month over Month across the Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019.

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

# Group by Month and Product Line
grouped_product_line = df.groupby(["Month", "Product line"]).agg({"Quantity": "sum", "Revenue": "sum"}).reset_index()

# Group by Month and Gender
grouped_gender = df.groupby(["Month", "Gender"]).agg({"Quantity": "sum", "Revenue": "sum"}).reset_index()

# Group by Month and Payment Method
grouped_payment = df.groupby(["Month", "Payment"]).agg({"Quantity": "sum", "Revenue": "sum"}).reset_index()

print(grouped_product_line)
print(grouped_gender)
print(grouped_payment)

# Plot sales and revenue by Product Line across months
plt.figure(figsize=(12, 6))
sns.lineplot(x="Month", y="Revenue", hue="Product line", data=grouped_product_line, marker="o")
plt.title("Revenue by Product Line - Month over Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Plot sales and revenue by Gender across months
plt.figure(figsize=(12, 6))
sns.lineplot(x="Month", y="Revenue", hue="Gender", data=grouped_gender, marker="o")
plt.title("Revenue by Gender - Month over Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Plot sales and revenue by Payment Method across months
plt.figure(figsize=(12, 6))
sns.lineplot(x="Month", y="Revenue", hue="Payment", data=grouped_payment, marker="o")
plt.title("Revenue by Payment Method - Month over Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()