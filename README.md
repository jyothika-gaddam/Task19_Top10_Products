# Task 19 – Top 10 Products

## Objective
Identify the top 10 products by total sales.

## Tools
- Excel
- Python
- Pandas
- Matplotlib

## Analysis Method
1. Load the Sample Superstore dataset.
2. Group records by `Product Name`.
3. Sum `Sales` for each product.
4. Sort products in descending order of total sales.
5. Select the top 10 products.
6. Create a horizontal bar chart for easy comparison.

## Top 10 Results

| Rank | Product | Total Sales |
|---:|---|---:|
| 1 | Canon imageCLASS 2200 Advanced Copier | $61,599.82 |
| 2 | Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind | $27,453.38 |
| 3 | Cisco TelePresence System EX90 Videoconferencing Unit | $22,638.48 |
| 4 | HON 5400 Series Task Chairs for Big and Tall | $21,870.58 |
| 5 | GBC DocuBind TL300 Electric Binding System | $19,823.48 |
| 6 | GBC Ibimaster 500 Manual ProClick Binding System | $19,024.50 |
| 7 | Hewlett Packard LaserJet 3310 Copier | $18,839.69 |
| 8 | HP Designjet T520 Inkjet Large Format Printer - 24" Color | $18,374.90 |
| 9 | GBC DocuBind P400 Electric Binding System | $17,965.07 |
| 10 | High Speed Automatic Electric Letter Opener | $17,030.31 |

## Key Insight
The Canon imageCLASS 2200 Advanced Copier is the clear #1 product by sales, with about $61.6K in total sales. Technology and office-equipment products dominate the top 10.

## Tie Check
There is no tie at the 10th-place cutoff, so the top 10 list is unambiguous.

## Deliverables
- `Task19_Top10_Products.xlsx` – Excel table and chart
- `data/top10_products_by_sales.csv` – Top-10 result table
- `charts/top10_products_by_sales.png` – Chart
- `scripts/top10_products_analysis.py` – Python analysis script
