budget = int(input())
sum_counter = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    current_price = float(command)

    if sum_counter + current_price > budget:
        print("You went in overdraft!")
        break

    sum_counter += current_price