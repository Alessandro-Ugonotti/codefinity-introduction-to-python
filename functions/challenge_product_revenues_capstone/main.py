# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue = []

for i in range(len(products)):
    revenue_item = prices[i]*quantities_sold[i]
    revenue += [revenue_item]

revenue_per_product = list(zip(products, revenue))
#revenue_per_product = sorted(list(zip(products, revenue)))

for i in range(len(revenue_per_product)):
    print(f"{revenue_per_product[i][0]} has total revenue of ${revenue_per_product[i][1]}.")

print("----")

def calculate_revenue(prices, quantities_sold):
    items = []
    for i in range(len(prices)):
        revenue_per_item = prices[i]*quantities_sold[i]
        items += [revenue_per_item]
        revenues = list(zip(products, items))
    return(revenues)

try1 = calculate_revenue(prices, quantities_sold)
print(try1)

def print_revenue(revenues):
    revenues = sorted(revenues)
    for i in range(len(revenues)):
        print(f"{revenues[i][0]} has total revenue of ${revenues[i][1]}.")

print_revenue(try1)