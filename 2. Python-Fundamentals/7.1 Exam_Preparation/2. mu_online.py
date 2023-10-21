given_string = input().split("|")
health = 100
bitcoins = 0
best_room = 0
for i in given_string:
    best_room += 1
    current_i = i.split()

    if current_i[0] == "potion":
        current_health = health
        health += int(current_i[1])
        if health > 100:
            health = 100
        amount_healed = health - current_health
        print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {health} hp.")

    elif current_i[0] == "chest":
        bitcoins += int(current_i[1])
        print(f"You found {int(current_i[1])} bitcoins.")

    else:
        health -= int(current_i[1])
        if health > 0:
            print(f"You slayed {current_i[0]}.")
        else:
            print(f"You died! Killed by {current_i[0]}.")
            print(f"Best room: {best_room}")
            break

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")