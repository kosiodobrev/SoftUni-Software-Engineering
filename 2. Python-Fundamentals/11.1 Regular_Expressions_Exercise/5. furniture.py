import re

command = input()
furniture = ""
price = 0
quantity = 0
total_price = 0
bought_items = []
pattern = r"\>+([A-Za-z0-9]+)\<+([0-9\.?]+)\!([0-9]+)\b"
while command != "Purchase":
    match = re.findall(pattern, command)
    if match:
        for item in match:
            furniture = item[0]
            price = float(item[1])
            quantity = int(item[2])
            total_price += quantity * price
            bought_items.append(furniture)
    else:
        command = input()
        continue

    furniture = ""
    price = 0
    quantity = 0
    command = input()

print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")
