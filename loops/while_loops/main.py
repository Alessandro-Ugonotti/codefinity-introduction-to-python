# Simulate a grocery store restocking process
stock = 12  # Current stock level
restock_goal = 20  # Desired stock level
restock_amount = 2  # Amount to add each restock

# Your code here
while stock < restock_goal:
    stock = stock + restock_amount
    if stock == restock_goal:
        print("Restocking complete!")
print(stock)
