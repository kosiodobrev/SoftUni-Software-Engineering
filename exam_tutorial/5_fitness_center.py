number_people = int(input())
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
for _ in range(number_people):
    action = input()
    if action == "Back":
        back_counter += 1
    elif action == "Chest":
        chest_counter += 1
    elif action == "Legs":
        legs_counter += 1
    elif action == "Abs":
        abs_counter += 1
    elif action == "Protein shake":
        protein_shake_counter += 1
    elif action == "Protein bar":
        protein_bar_counter += 1

percent_work_out = (back_counter + chest_counter + legs_counter + abs_counter) / number_people * 100
percent_protein = (protein_bar_counter + protein_shake_counter) / number_people * 100

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{percent_work_out:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
