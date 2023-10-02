gifts = input().split()
while True:
    command = input().split()
    if command == ["No", "Money"]:
        break
    if command[0] == "OutOfStock":
        for items in range(len(gifts)):
            if gifts[items] == command[1]:
                gifts[items] = "None"

    elif command[0] == "Required":
        gift_index = int(command[2])
        if 0 <= gift_index < len(gifts):
            gifts[gift_index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

filtered_gifts = [s for s in gifts if s != "None"]
print(" ".join(filtered_gifts))



