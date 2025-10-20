# Sales Data Analysis Project using NumPy, Pandas, and Matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
print("✅ Data Loaded Successfully!")
print(df.head())  # Show first 5 rows

# Data Cleaning & Derived Columns
# Create new calculated columns
df['Revenue'] = np.multiply(df['Units_Sold'], df['Unit_Price'])
df['Total_Profit'] = np.multiply(df['Units_Sold'], df['Profit_Per_Unit'])

# Profit margin %
df['Profit_Margin'] = df['Profit_Per_Unit'] / df['Unit_Price']


# Category-wise summary
category_summary = df.groupby('Category').agg({
    'Revenue': "sum", 
    'Total_Profit': "sum", 
    "Profit_Margin": "sum"

}).sort_values('Revenue', ascending=False)

print('\nCategory_wise summary:')
print(category_summary)

# Region-wise Summary
region_summary = df.groupby('Region')[['Revenue', 'Total_Profit']].sum()
print('\nRegion_wise summary:')
print(region_summary)

# Monthly Trend Analysis
df['Month'] = df['Date'].dt.to_period('M')
Monthly_trend = df.groupby('Month')[['Revenue', 'Total_Profit']].sum()
Monthly_trend['Revenue_MA'] = Monthly_trend['Revenue'].rolling(window=3).mean()
print('\nMonthly_trend:')
print(Monthly_trend)

# 6️⃣ NumPy Statistical Insights

revenue_array = df['Revenue'].to_numpy()
print("\nStatistical Insights:")
print('Mean Revenue:', np.mean(revenue_array))
print('Median Revenue:', np.median(revenue_array))
print('Revenue Std Deviation:', np.std(revenue_array))
print('90th Percentile Revenue:', np.percentile(revenue_array, 90))

# Visualization — Monthly Revenue Trend
plt.figure(figsize=(8,5))
plt.plot(Monthly_trend.index.astype(str), Monthly_trend['Revenue'], label='Revenue')
plt.plot(Monthly_trend.index.astype(str), Monthly_trend['Revenue_MA'], label='Moving Avg', linestyle='--')
plt.legend()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#  Visualization — Category-wise Revenue (Bar Chart)
plt.figure(figsize=(7,5))
plt.bar(category_summary.index, category_summary['Revenue'], color='skyblue')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Visualization — Region-wise Profit (Pie Chart)
plt.figure(figsize=(6,6))
plt.pie(region_summary['Total_Profit'], labels=region_summary.index, autopct='%1.1f%%', startangle=90)
plt.title("Profit Distribution by Region")
plt.tight_layout()
plt.show()

