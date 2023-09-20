while True:
    destination = input()
    if destination == "End":
        break
    needed_budget = float(input())
    saved_money_counter = 0
    enough_savings = False
    while saved_money_counter < needed_budget:
        current_savings = float(input())
        saved_money_counter += current_savings
        if saved_money_counter >= needed_budget:
            enough_savings = True
            break
    if enough_savings:
        print(f"Going to {destination}!")
