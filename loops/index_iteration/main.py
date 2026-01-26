prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.9, 0.8, 0.85, 0.95]
# Write your code here
for i in range(len(prices)):
    prices[i] = prices[i]*discounts[i]
    print(f"Updated price for item {i}: ${prices[i]:.2f}")