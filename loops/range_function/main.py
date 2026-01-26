# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Write your code here
for i in range(0,5,1):
    weekday = weekdays[i]
    promotion = daily_promotions[i]
    print(f"{weekday}: Promotion on {promotion}")
