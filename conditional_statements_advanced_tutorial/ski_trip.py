days_stayed = int(input())
type_room = input()
feedback = input()
room_one_person_per_night = 18
apartment_per_night = 25
president_apartment_per_night = 35
discounted_end_price = 0
nights_stayed = days_stayed - 1
end_price = 0

if days_stayed < 10:
    if type_room == "room for one person":
        end_price += room_one_person_per_night
    elif type_room == "apartment":
        end_price += (apartment_per_night * 0.7)
    elif type_room == "president apartment":
        end_price += (president_apartment_per_night * 0.9)
if 10 <= days_stayed < 15:
    if type_room == "room for one person":
        end_price += room_one_person_per_night
    elif type_room == "apartment":
        end_price += apartment_per_night * 0.65
    elif type_room == "president apartment":
        end_price += president_apartment_per_night * 0.85
if days_stayed > 15:
    if type_room == "room for one person":
        end_price += room_one_person_per_night
    elif type_room == "apartment":
        end_price += apartment_per_night * 0.5
    elif type_room == "president apartment":
        end_price += president_apartment_per_night * 0.80

price_all = end_price * nights_stayed

if feedback == "positive":
    price_all *= 1.25
elif feedback == "negative":
    price_all *= 0.9

print(f"{price_all:.2f}")