price = input()
price_with_tax = 0
total_price_without_taxes = 0
total_taxes = 0
taxes_price = 0
total_price = 0
while True:
    total_price_without_taxes += float(price)
    taxes_price = float(price) * 0.2
    total_taxes += taxes_price
    total_price += (float(price) + taxes_price)


    if not float(price) > 0:
        print("Invalid price!")
    price = input()
    if price != "special" or price != "regular":
        break

if price_with_tax == 0:
        print("Invalid order!")
if price == "special":
    price_with_tax *= 0.9

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price_without_taxes:.2f}$")
print(f"Taxes: {total_taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")