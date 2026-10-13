
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset
file_path = Path("Sample-Superstore.csv")
df = pd.read_csv(file_path)

# Basic data inspection
print("SALES DATA ANALYSIS")
print("=" * 40)
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Convert date column
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

# Calculate key metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
profit_margin = (total_profit / total_sales) * 100

print("\nKEY BUSINESS METRICS")
print("=" * 40)
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Units Sold: {total_quantity:,}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

# Monthly sales trend
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# Category performance
category_sales = df.groupby("Category")[
    ["Sales", "Profit", "Quantity"]
].sum()

print("\nCATEGORY PERFORMANCE")
print(category_sales)

# Save category chart
sns.set_theme(style="whitegrid")
category_sales["Sales"].sort_values().plot(
    kind="barh", figsize=(9, 5)
)
plt.title("Total Sales by Product Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("category_sales.png", dpi=300)
plt.show()


# Monthly Sales Trend Chart
monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend (2014–2017)", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()

print("Chart saved as category_sales.png")
print("Chart saved as monthly_sales_trend.png")


# Quarterly Sales Analysis
df["Quarter"] = df["Order Date"].dt.to_period("Q")

quarterly_sales = df.groupby("Quarter")["Sales"].sum()

print("\nQUARTERLY SALES ANALYSIS")
print(quarterly_sales)

plt.figure(figsize=(10, 5))
quarterly_sales.plot(kind="bar")

plt.title("Quarterly Sales Trend (2014–2017)")
plt.xlabel("Quarter")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("quarterly_sales.png", dpi=300)
plt.show()

print("Chart saved as quarterly_sales.png")


# Profit Analysis by Category
category_profit = df.groupby("Category")["Profit"].sum()

print("\nPROFIT ANALYSIS BY CATEGORY")
print(category_profit)

plt.figure(figsize=(9, 5))
category_profit.sort_values().plot(kind="barh")

plt.title("Profit by Product Category")
plt.xlabel("Total Profit ($)")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig("category_profit.png", dpi=300)
plt.show()

print("Chart saved as category_profit.png")


# Geographic Sales Analysis
region_sales = df.groupby("Region")["Sales"].sum().sort_values()

print("\nREGION-WISE SALES")
print(region_sales)

plt.figure(figsize=(9, 5))
region_sales.plot(kind="barh")

plt.title("Total Sales by Region")
plt.xlabel("Total Sales ($)")
plt.ylabel("Region")
plt.tight_layout()

plt.savefig("region_sales.png", dpi=300)
plt.show()

print("Chart saved as region_sales.png")


# Sub-Category Performance Analysis
subcategory_performance = df.groupby("Sub-Category")[
    ["Sales", "Profit", "Quantity"]
].sum().sort_values("Sales", ascending=False)

print("\nSUB-CATEGORY PERFORMANCE")
print(subcategory_performance)

plt.figure(figsize=(11, 7))
subcategory_performance["Sales"].sort_values().plot(
    kind="barh"
)

plt.title("Sales Performance by Sub-Category")
plt.xlabel("Total Sales ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("subcategory_sales.png", dpi=300)
plt.show()

print("Chart saved as subcategory_sales.png")


# Seasonal Sales Analysis
df["Month_Name"] = df["Order Date"].dt.month_name()
df["Month_Number"] = df["Order Date"].dt.month

seasonal_sales = df.groupby(
    ["Month_Number", "Month_Name"]
)["Sales"].mean().reset_index()

seasonal_sales = seasonal_sales.sort_values("Month_Number")

print("\nAVERAGE SALES BY MONTH")
print(seasonal_sales[["Month_Name", "Sales"]])

plt.figure(figsize=(11, 6))
plt.bar(
    seasonal_sales["Month_Name"],
    seasonal_sales["Sales"]
)

plt.title("Average Sales by Month (Seasonal Pattern)")
plt.xlabel("Month")
plt.ylabel("Average Sales per Record ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("seasonal_sales.png", dpi=300)
plt.show()

print("Chart saved as seasonal_sales.png")


# Average Order Value (AOV)
total_orders = df["Order ID"].nunique()
aov = df["Sales"].sum() / total_orders

print("\nAVERAGE ORDER VALUE ANALYSIS")
print("Total Unique Orders:", total_orders)
print(f"Average Order Value: ${aov:,.2f}")

# Top 10 Products by Sales
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY SALES")
print(top_products)

plt.figure(figsize=(11, 7))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.savefig("top_10_products.png", dpi=300)
plt.show()

print("Chart saved as top_10_products.png")
