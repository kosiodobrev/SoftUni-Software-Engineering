def fire_func(warship, index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage

        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()

def defend_func(pirateship, startIndex, endIndex, damage):
    if 0 <= startIndex < len(pirate_ship) and 0 <= endIndex < len(pirateship):
        for i in range(startIndex, endIndex + 1):
            pirateship[i] -= damage

            if pirateship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()

def repair_func(pirate_ship, index, health, max_health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)

def status_func(pirate_ship, max_health):
    count = sum(1 for section in pirate_ship if section < 0.2 * max_health)
    print(f"{count} sections need repair.")

pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input().split()

    current_command = command[0]

    if current_command == "Retire":
        break

    elif current_command == "Fire":
        index, damage = int(command[1]), int(command[2])
        fire_func(warship, index, damage)

    elif current_command == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        defend_func(pirate_ship, start_index, end_index, damage)

    elif current_command == "Repair":
        index, health = int(command[1]), int(command[2])
        repair_func(pirate_ship, index, health, max_health)

    elif current_command == "Status":
        status_func(pirate_ship, max_health)

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")