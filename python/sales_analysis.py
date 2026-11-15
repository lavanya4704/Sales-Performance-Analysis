
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 1. Set project paths
ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "sales.csv"
OUTPUT_DIR = ROOT / "data" / "processed"
CHART_DIR = ROOT / "screenshots"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

# 2. Load dataset
df = pd.read_csv(RAW_FILE, encoding="cp1252")
print("Dataset loaded:", df.shape)

# 3. Clean column names
df.columns = df.columns.str.strip()

# 4. Remove duplicate rows
before = len(df)
df = df.drop_duplicates()
print("Duplicate rows removed:", before - len(df))

# 5. Convert dates and numeric columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"], dayfirst=True, errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], dayfirst=True, errors="coerce"
)

numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 6. Remove rows with invalid essential values
df = df.dropna(
    subset=[
        "Order Date", "Order ID", "Region",
        "Category", "Product Name",
        "Sales", "Quantity", "Profit"
    ]
)

df = df[df["Quantity"] > 0]

# 7. Create useful date columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%b")
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# 8. Save cleaned dataset
clean_file = OUTPUT_DIR / "sales_clean.csv"
df.to_csv(clean_file, index=False, encoding="utf-8-sig")

print("\nDATA CLEANING COMPLETED")
print("Rows after cleaning:", len(df))
print("Cleaned file saved to:", clean_file)

# 9. Calculate business KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

profit_margin = (
    total_profit / total_sales * 100 if total_sales else 0
)

print("\nSALES PERFORMANCE SUMMARY")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,.0f}")
print(f"Total Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# 10. Monthly sales trend
monthly_sales = (
    df.groupby("Year-Month", as_index=False)["Sales"]
    .sum()
    .sort_values("Year-Month")
)

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x="Year-Month", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_sales.png", dpi=300)
plt.close()

# 11. Sales by region
region_sales = (
    df.groupby("Region", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

plt.figure(figsize=(9, 5))
sns.barplot(data=region_sales, x="Region", y="Sales")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(CHART_DIR / "sales_by_region.png", dpi=300)
plt.close()

# 12. Top 10 products by sales
top_products = (
    df.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
    .sort_values("Sales")
)

plt.figure(figsize=(12, 7))
sns.barplot(data=top_products, x="Sales", y="Product Name")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "top_products.png", dpi=300)
plt.close()

# 13. Category performance
category_summary = (
    df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print("\nCATEGORY PERFORMANCE")
print(category_summary.to_string(index=False))

# 14. Loss-making products
product_profit = (
    df.groupby("Product Name", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit")
)

print("\nBOTTOM 10 PRODUCTS BY PROFIT")
print(product_profit.head(10).to_string(index=False))

print("\nCharts saved in:", CHART_DIR)
print("NEXT: Check the processed CSV and three chart images.")