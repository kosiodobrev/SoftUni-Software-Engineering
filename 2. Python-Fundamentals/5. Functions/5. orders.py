def orders(product,quantity):
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    if product == "coffee":
        return f"{coffee * quantity:.2f}"
    elif product == "coke":
        return f"{coke * quantity:.2f}"
    elif product == "water":
        return f"{water * quantity:.2f}"
    elif product == "snacks":
        return f"{snacks * quantity:.2f}"

prouduct = inpt()
quantity = int(input())
result = orders(product, quantity)
print(result)