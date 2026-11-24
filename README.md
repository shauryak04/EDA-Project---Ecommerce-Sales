# E-commerce Sales – Exploratory Data Analysis

Analyse e-commerce transactions to find revenue trends over time, top-earning categories, and preferred payment methods.

## Dataset

**File:** `data/ecommerce_sales.csv`

Key columns used:

- Date – transaction date
- Category – product category
- Quantity
- UnitPrice
- Discount – discount in percent
- PaymentMode

## What the analysis does

1. Convert `Date` to datetime and extract `Month` and `Weekday`
2. Engineer revenue features: `Gross = Quantity × UnitPrice` and `NetAmount = Gross × (1 − Discount/100)`
3. Inspect structure, statistics and category counts
4. Check for missing values and duplicate rows
5. Aggregate net revenue by month, weekday and category (in calendar order)
6. Count transactions by payment mode

## Visualisations

| Chart | Type |
|-------|------|
| Total Sales by Month | Bar chart of net revenue |
| Sales by Weekday | Bar chart of net revenue |
| Category-wise Revenue | Bar chart |
| Payment Mode Count | Bar chart |

## Questions explored

- Which month and weekday bring in the most revenue?
- Which product categories earn the most?
- What payment modes do customers prefer?

## Key insights

<!-- Run the script and write 3–5 findings here, e.g. "Customers in X had the highest ..." -->

- _Add your findings here_

## How to run

From the root of the repository:

```bash
pip install -r requirements.txt
python 05_ecommerce_sales_eda/ecommerce_sales_eda.py
```

Make sure `ecommerce_sales.csv` is in the `data/` folder. Each chart opens in a window; close it to see the next one.

## Tools

Python · pandas · matplotlib · seaborn

---
[← Back to all projects](../README.md)
