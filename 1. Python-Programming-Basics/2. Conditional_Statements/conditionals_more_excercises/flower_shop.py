from math import floor
from math import ceil
number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_cactus = int(input())
gift_price = float(input())

magnolii = number_magnolii * 3.25
zumbuli = number_zumbuli * 4
roses = number_roses * 3.50
cactus = number_cactus * 8

total_sum = magnolii + zumbuli + roses + cactus
total_sum_after_tax = total_sum - (total_sum * 0.05)

difference = abs(total_sum_after_tax - gift_price)

if total_sum_after_tax >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")