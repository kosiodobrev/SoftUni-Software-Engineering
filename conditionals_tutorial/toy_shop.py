needed_money = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_sum = number_of_puzzles * 2.60 \
            + number_of_dolls * 3 \
            + number_of_bears * 4.10 \
            + number_of_minions * 8.20 \
            + number_of_trucks * 2

total_toys = number_of_puzzles \
             + number_of_dolls \
             + number_of_bears \
             + number_of_minions \
             + number_of_trucks

if total_toys >= 50:
    total_sum = total_sum * 0.75
total_sum = total_sum * 0.90

difference = abs(total_sum - needed_money)

if total_sum >= needed_money:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
