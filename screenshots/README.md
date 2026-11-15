# Sales Performance Analysis and Business Intelligence Dashboard

## Project Overview

The **Sales Performance Analysis and Business Intelligence Dashboard** is a data analytics project that analyzes retail sales data to understand business performance, identify sales trends, evaluate profitability, and discover top-performing and loss-making products.

The project uses Python for data cleaning and analysis, SQL for data querying, and Looker Studio to create an interactive business intelligence dashboard.

## Project Objectives

- Analyze overall sales and profit performance.
- Identify monthly sales and profit trends.
- Compare sales and profitability across regions and categories.
- Identify the top 10 products by sales and profit.
- Identify products generating losses.
- Present business insights through an interactive dashboard.

## Tools and Technologies

- **Programming:** Python
- **Libraries:** Pandas, NumPy, Matplotlib
- **Database Querying:** SQL
- **Data Visualization:** Looker Studio
- **Data Source:** Google Sheets

## Key Features

- Data cleaning and preprocessing using Python.
- Sales and profit analysis.
- Monthly sales and profit trend analysis.
- Regional and category-wise performance analysis.
- Top 10 products by sales.
- Top 10 products by profit.
- Loss-making product identification.
- Interactive dashboard with Region, Category, Segment, and Date filters.

## Live Dashboard

**[View Interactive Sales Performance Dashboard](https://datastudio.google.com/reporting/105c31ab-d924-47eb-a1d9-e51c82fc7429)**

## Dashboard Preview

### Sales Overview
![Sales Overview](screenshots/sales_overview.png)

### Product Analysis
![Product Analysis](screenshots/product_analysis.png)

## Project Structure

```text
Sales-Performance-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── python/
│   └── sales_analysis.py
│
├── sql/
│   └── analysis_queries.sql
│
├── screenshots/
│   ├── sales_overview.png
│   ├── product_analysis.png
│   ├── monthly_sales.png
│   ├── sales_by_region.png
│   └── top_products.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/lavanya4704/Sales-Performance-Analysis.git
```

### 2. Navigate to the project folder

```bash
cd Sales-Performance-Analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python analysis

```bash
python python/sales_analysis.py
```

The analysis script processes the sales dataset, performs data analysis, and generates visualizations.

## SQL Analysis

The SQL queries cover:

- Overall sales and profit.
- Regional performance.
- Category-wise analysis.
- Monthly sales trends.
- Top-performing products.
- Loss-making products.

## Author

**Lavanya Singamsetti**

B.Tech – Computer Science (AI & Data Science)

[GitHub](https://github.com/lavanya4704) | [LinkedIn](https://linkedin.com/in/lavanya-singamsetti-6a41b232a/)