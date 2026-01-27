# Grocery store inventory:
# "Item": [current stock, target stock level, restock amount]
inventory = {
    "Bread": [30, 50, 10],
    "Eggs": [120, 200, 40],
    "Milk": [60, 100, 20],
    "Apples": [15, 50, 15]
}

print("Restocking started")

# Write your code here
for i in inventory:
    while inventory[i][0] < inventory[i][1]:
        inventory[i][0] += inventory[i][2]
        print(f"restocking {i} to: {inventory[i][0]}")

print("Restocking completed")