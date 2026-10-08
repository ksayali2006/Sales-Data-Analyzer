A short Python project that uses **Pandas** and **NumPy** to analyse shop sales.

## What it does
- Stores product, price and quantity in a DataFrame
- Calculates revenue per product (Price x Qty)
- Marks each product as High or Low sales using `np.where()` (High if revenue >= 1500)
- Prints the total revenue and the best-selling product

## Requirements
- Python 3.8+
- pandas, numpy

## How to run
```bash
pip install -r requirements.txt
python sales_analyzer.py
```

## Output
```
  Product  Price  Qty  Revenue Status
0     Pen     10   50      500    Low
1    Book    120   20     2400   High
2     Bag    450    8     3600   High
3  Bottle     80   15     1200    Low
4  Pencil      5  100      500    Low
Total Revenue: 8200
Best Seller: Bag
```

## Author
Sayali Kadalagekar - Python Programming OJT, 2026-27
