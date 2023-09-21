from math import ceil
number_people = int(input())
entrance_fee = float(input())
shezlong_price = float(input())
umbrella_price = float(input())

sum_from_tax = number_people * entrance_fee  #115.60
sum_shezlong = (ceil(number_people * 0.75)) * shezlong_price  #70.40
sum_umbrella = (ceil(number_people / 2)) * umbrella_price   #68.20
sum = sum_from_tax + sum_shezlong + sum_umbrella

print(f'{sum: .2f}' + " lv.")