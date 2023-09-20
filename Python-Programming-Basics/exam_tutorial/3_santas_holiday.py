days = int(input())
type_of_room = input()
feedback = input()
final_price = 0
nights = days - 1
if days < 10:
    if type_of_room == "room for one person":
        final_price = nights * 18
    elif type_of_room == "apartment":
        final_price = (nights * 25) * 0.7
    elif type_of_room == "president apartment":
        final_price = (nights * 35) * 0.9
elif 10 <= days <= 15:
    if type_of_room == "room for one person":
        final_price = nights * 18
    elif type_of_room == "apartment":
        final_price = (nights * 25) * 0.65
    elif type_of_room == "president apartment":
        final_price = (nights * 35) * 0.85
elif days > 15:
    if type_of_room == "room for one person":
        final_price = nights * 18
    elif type_of_room == "apartment":
        final_price = (nights * 25) * 0.5
    elif type_of_room == "president apartment":
        final_price = (nights * 35) * 0.8

if feedback == "positive":
    final_price = final_price + (final_price * 0.25)
elif feedback == "negative":
    final_price *= 0.9

print(f"{final_price:.2f}")