needed_money = float(input())
available_money = float(input())
spending_days_in_a_row = 0
days_counter = 0
while True:
    text = input()
    sum_spend_saved = float(input())
    if text == "spend":
        spending_days_in_a_row += 1
        if sum_spend_saved >= available_money:
            available_money = 0
        else:
            available_money -= sum_spend_saved
    elif text == "save":
        spending_days_in_a_row = 0
        available_money += sum_spend_saved
    days_counter += 1
    if spending_days_in_a_row == 5:
        print("You can't save the money.")
        print(f"{days_counter}")
        break
    elif available_money >= needed_money:
        print(f"You saved the money for {days_counter} days.")
        break
