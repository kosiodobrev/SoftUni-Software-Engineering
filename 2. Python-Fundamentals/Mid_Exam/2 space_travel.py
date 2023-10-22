travel_route_to_titan = input().split("||")
starting_fuel = int(input())
starting_ammu = int(input())

for current_command in travel_route_to_titan:
    command = current_command.split(" ")
    event = command[0]
    if event == "Travel":
        light_years = int(command[1])
        if starting_fuel >= light_years:
            starting_fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif event == "Enemy":
        enemy_armour = int(command[1])
        if starting_ammu >= enemy_armour:
            starting_ammu -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            needed_fuel = enemy_armour * 2
            if starting_fuel > needed_fuel:
                starting_fuel -= needed_fuel
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif event == "Repair":
        added_ammu_fuel = int(command[1])
        starting_fuel += added_ammu_fuel
        starting_ammu += added_ammu_fuel * 2
        print(f"Ammunitions added: {added_ammu_fuel * 2}.")
        print(f"Fuel added: {added_ammu_fuel}.")

    elif event == "Titan":
        print("You have reached Titan, all passengers are safe.")
        exit()




