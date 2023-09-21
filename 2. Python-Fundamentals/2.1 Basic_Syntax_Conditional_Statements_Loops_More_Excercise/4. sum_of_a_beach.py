string = input()
lower_string = string.lower()
count = 0
count_sand = lower_string.count("sand")
count_water = lower_string.count("water")
count_fish = lower_string.count("fish")
count_sun = lower_string.count("sun")
counter = count_fish + count_sun + count_water + count_sand
print(counter)