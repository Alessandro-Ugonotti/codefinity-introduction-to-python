# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, values in products.items():
    # Calculate total_sales here
    total_sales = float(values[0])*int(values[1])
    print(f"Total sales for {product}: ${total_sales}")
    # Add to total_sales_list here
    total_sales_list += [total_sales]
    print(total_sales_list)
# Calculate total_sum here
total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")
# Calculate min_sales here
min_sales = min(total_sales_list)
print(f"Minimum sales: ${min_sales}")
# Calculate max_sales here
max_sales = max(total_sales_list)
print(f"Maximum sales: ${max_sales}")