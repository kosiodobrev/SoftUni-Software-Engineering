price_kg_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

price_strawberries = price_kg_strawberries * kg_strawberries
price_kg_raspberries = price_kg_strawberries * 0.5
price_kg_oranges = price_kg_raspberries * 0.6
price_kg_bananas = price_kg_raspberries * 0.2

price_bananas = price_kg_bananas * kg_bananas
price_oranges = price_kg_oranges * kg_oranges
price_raspberries = price_kg_raspberries * kg_raspberries

total_price = price_strawberries + price_oranges + price_bananas + price_raspberries

print(f"{total_price:.2f}")