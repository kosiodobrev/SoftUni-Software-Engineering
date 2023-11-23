products_dict = {}
command = input()
while command != "buy":
    name, price, quantity = command.split(" ")
    price = float(price)
    quantity = int(quantity)

    if name not in products_dict:
        products_dict[name] = []
        products_dict[name].append(price)
        products_dict[name].append(quantity)
    else:
        products_dict[name][0] = price
        products_dict[name][1] += quantity

    command = input()

for key, value in products_dict.items():

    print(f"{key} -> {(value[0] * value[1]):.2f}")