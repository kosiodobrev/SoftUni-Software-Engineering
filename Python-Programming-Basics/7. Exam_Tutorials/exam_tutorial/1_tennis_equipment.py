from math import ceil
from math import floor
tennis_rocket_price = float(input())
number_tennis_rockets = int(input())
number_sneakers = int(input())

final_tennis_rocket_price = tennis_rocket_price * number_tennis_rockets
price_sneakers = 1/6 * tennis_rocket_price
final_sneakers_price = price_sneakers * number_sneakers
price_rocket_sneakers = final_sneakers_price + final_tennis_rocket_price
other_equipment = price_rocket_sneakers * 0.2
full_price = price_rocket_sneakers + other_equipment
price_to_be_paid_by_djokovic = floor(1/8 * full_price)
price_to_be_paid_by_sponsors = ceil(7/8 * full_price)

print(f"Price to be paid by Djokovic {price_to_be_paid_by_djokovic}")
print(f"Price to be paid by sponsors {price_to_be_paid_by_sponsors}")