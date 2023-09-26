n = int(input())
tank_capacity = 255
water_counter = 0
for i in range(n):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    water_counter += liters_of_water
print(water_counter)