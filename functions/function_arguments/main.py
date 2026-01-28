def apply_discount(price, discount=0.10):
    price = price * (1 - discount)
    return(price)

def add_tax(price, tax=0.05):
    price = price * (1 + tax)
    return(price)

def final_price(price, discount=0.10, tax=0.05):
    discounted = apply_discount(price, discount)
    taxed = add_tax(discounted, tax)
    return(taxed)

value1 = round(final_price(50), 2)
print(f"Final price with default discount and tax: ${value1}.")

value2 = round(final_price(50, tax=0.08), 2)
print(f"Final price with custom tax: ${value2}.")