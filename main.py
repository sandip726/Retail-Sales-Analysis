import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore.csv",encoding="UTF-8")
#Convert to Datetime
print(df.info())
df["Order Date"]= pd.to_datetime(df["Order Date"],dayfirst=True)
df["Ship Date"]= pd.to_datetime(df["Ship Date"],dayfirst=True)

#Handiling missing value
df.dropna(axis=0,inplace=True)
df["Postal Code"]=df["Postal Code"].astype(int)

average_sales = df["Sales"].mean()
Highest_sales = df["Sales"].max()
lowest_sales = df["Sales"].min()

print(f"The average of sales:",average_sales)
print(f"The Highest of sales:",Highest_sales)
print(f"The lowest of sales:",lowest_sales)

#Aggregation 
sales_by_segments = df.groupby("Segment")["Sales"].sum()
print(sales_by_segments)

sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)

#Time series analysis
df_time = df.set_index("Order Date")
#Monthly sales 
monthly_sales = df_time["Sales"].resample("ME").sum()
print("\n --Monthly Sales--")
print(monthly_sales.head(12))

highest_sales_monthly = monthly_sales.idxmax()
highest_sales_value = monthly_sales.max()
print(f"\nHighest Sales Month: {highest_sales_monthly.strftime('%Y-%m')} with ${highest_sales_value}")

# --- A. Time-Series Plot (Monthly Sales) ---
plt.figure(figsize=(12, 6))
# Plot the monthly sales data
monthly_sales.plot(kind='line', marker='o', linestyle='-', linewidth=1, markersize=3)
plt.title('Monthly Sales Trend (2015-2018)', fontsize=16)
plt.xlabel('Order Date', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()


#  Bar Plot for Segment Sales ---
plt.figure(figsize=(12, 6))
# Use the calculated sales_by_segments Series
sales_by_segments.sort_values(ascending=False).plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Total Sales by Customer Segment', fontsize=14)
plt.xlabel('Customer Segment')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0) # Keeps labels horizontal
plt.tight_layout()
plt.show()

# Bar Plot for Category Sales ---
plt.figure(figsize=(12, 6))
# Use the calculated sales_by_category Series
sales_by_category.sort_values(ascending=False).plot(kind='bar', color=['gold', 'darkorange', 'purple'])
plt.title('Total Sales by Product Category', fontsize=14)
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()