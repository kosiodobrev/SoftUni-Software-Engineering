number_bottles = int(input())
liquid_per_bottle = 750
all_liquid = liquid_per_bottle * number_bottles   #1500
needed_liquid_plate = 5
needed_liquid_pot = 15
dishwasher_filling_counter = 0
number_plates = input()
washed_plates = 0
washed_pots = 0
used_liquid_plate = 0
used_liquid_pot = 0
is_the_liquid_enough = False
while number_plates != "End":
    dishwasher_filling_counter += 1
    if dishwasher_filling_counter % 3 == 0:
        used_liquid_pot = int(number_plates) * 15
        washed_pots += int(number_plates)
        all_liquid -= used_liquid_pot
    else:
        used_liquid_plate = int(number_plates) * 5
        washed_plates += int(number_plates)
        all_liquid -= used_liquid_plate
    if all_liquid < 0:
        break
    number_plates = input()
    if number_plates == "End":
        is_the_liquid_enough = True

if is_the_liquid_enough:
    print("Detergent was enough!")
    print(f"{washed_plates} dishes and {washed_pots} pots were washed.")
    print(f"Leftover detergent {all_liquid} ml.")
else:
    print(f"Not enough detergent, {abs(all_liquid)} ml. more necessary!")

