needed_sum = int(input())
price_item = input()
total_money = 0
counter_cash_card = 0
cash_payment = False
card_payment = False
times_paid_with_cash = 0
times_paid_with_card = 0
sum_cash = 0
sum_card = 0
while price_item != "End":
    if counter_cash_card == 0:
        cash_payment = True
        if int(price_item) > 100:
            cash_payment = False
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_money += int(price_item)
            times_paid_with_cash += 1
            sum_cash += int(price_item)
    price_item = input()
    counter_cash_card += 1
    if counter_cash_card == 1:
        card_payment = True
        if int(price_item) < 10:
            card_payment = False
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_money += int(price_item)
            times_paid_with_card += 1
            sum_card += int(price_item)
    counter_cash_card -= 1
    if total_money >= needed_sum:
        average_cs = sum_cash / times_paid_with_cash
        average_cc = sum_card / times_paid_with_card
        print(f"Average CS: {average_cs:.2f}")
        print(f"Average CC: {average_cc:.2f}")
        break
    price_item = input()
    if price_item == "End":
        print("Failed to collect required money for charity.")


