stage_tournament = input()
type_ticket = input()
number_tickets = int(input())
trophy_picture = input()
total_money = 0
trophy_picture_sum = 40 * number_tickets
if stage_tournament == "Quarter final":
    if type_ticket == "Standard":
        total_money += 55.5 * number_tickets
    elif type_ticket == "Premium":
        total_money += 105.2 * number_tickets
    elif type_ticket == "VIP":
        total_money += 118.9 * number_tickets
elif stage_tournament == "Semi final":
    if type_ticket == "Standard":
        total_money += 75.88 * number_tickets
    elif type_ticket == "Premium":
        total_money += 125.22 * number_tickets
    elif type_ticket == "VIP":
        total_money += 300.40 * number_tickets
elif stage_tournament == "Final":
    if type_ticket == "Standard":
        total_money += 110.10 * number_tickets
    elif type_ticket == "Premium":
        total_money += 160.66 * number_tickets
    elif type_ticket == "VIP":
        total_money += 400 * number_tickets
if total_money >= 4000:
    total_money_discounted = total_money * 0.75
    print(f"{total_money_discounted:.2f}")
elif total_money >= 2500:
    total_money_discounted = total_money * 0.90
    if trophy_picture == "Y":
        total_money_discounted += trophy_picture_sum
        print(f"{total_money_discounted:.2f}")
    elif trophy_picture == "N":
        print(f"{total_money_discounted:.2f}")
elif total_money < 2500:
    if trophy_picture == "Y":
        total_money += trophy_picture_sum
        print(f"{total_money:.2f}")
    elif trophy_picture == "N":
        print(f"{total_money:.2f}")






