# Initial apple stock in the store
apple_stock = 12
# Minimum required stock for apples
min_apple_stock = 40
# Number of apples the worker can restock per trip
restock_amount = 10

# Use a while loop to restock apples until the minimum stock is reached
# Your code here
while apple_stock <= min_apple_stock:
    print("Restocking apples...")
    apple_stock += restock_amount

# After restocking, print the final stock
print(f"Apple stock is now: {apple_stock} units.")