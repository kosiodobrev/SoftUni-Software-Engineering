level_of_fire = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
list_of_cells = []
for index in level_of_fire:
    type_of_fyre, value_of_cell = index.split(" = ")
    value_of_cell_integer = int(value_of_cell)
    if type_of_fyre == "High":
        if 81 <= value_of_cell_integer <= 125:
            if water >= value_of_cell_integer:
                water -= value_of_cell_integer
                total_effort += value_of_cell_integer * 0.25
                total_fire += value_of_cell_integer
                list_of_cells.append(value_of_cell_integer)
    elif type_of_fyre == "Medium":
        if 51 <= value_of_cell_integer <= 80:
            if water >= value_of_cell_integer:
                water -= value_of_cell_integer
                total_effort += value_of_cell_integer * 0.25
                total_fire += value_of_cell_integer
                list_of_cells.append(value_of_cell_integer)
    elif type_of_fyre == "Low":
        if 1 <= value_of_cell_integer <= 50:
            if water >= value_of_cell_integer:
                water -= value_of_cell_integer
                total_effort += value_of_cell_integer * 0.25
                total_fire += value_of_cell_integer
                list_of_cells.append(value_of_cell_integer)
print("Cells:")
for item in list_of_cells:
    print(f" - {item}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
