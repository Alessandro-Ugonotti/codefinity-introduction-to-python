grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
}
# Discount Eggs
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category_eggs, price_eggs, stock_eggs = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category_eggs, price_eggs - 1, stock_eggs)
#Add a New Item
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:" ,grocery_inventory)

#Restock Milk
if grocery_inventory["Milk"][2] <10:
    print("Milk needs to be restocked. increasing stock by 20 units.")
    category_milk, price_milk, stock_milk = grocery_inventory["Milk"] 
    grocery_inventory["Milk"] = (category_milk, price_milk, stock_milk +20) 
print("Updated inventory: ",grocery_inventory)