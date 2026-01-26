# Products and their current stock
products = [["Apples", 10], ["Bananas", 8]]

# Units sold today (same order as products)
units_sold = [3, 5]
for i in range(len(products)):
    products[i][1] -= units_sold[i]
print(f"Final stock levels:", products)