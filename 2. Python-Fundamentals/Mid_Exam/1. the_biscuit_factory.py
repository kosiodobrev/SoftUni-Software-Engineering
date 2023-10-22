from math import floor
biscuits_per_day = int(input())
workers = int(input())
enemy_factory_biscuits = int(input())
production = 0
for day in range(1, 31):
    daily_biscuits = biscuits_per_day * workers
    if day % 3 == 0:
        daily_biscuits *= 0.75
    production += floor(daily_biscuits)
print(f"You have produced {production} biscuits for the past month.")
if production > enemy_factory_biscuits:
    difference = production - enemy_factory_biscuits
    percentage = (difference / enemy_factory_biscuits) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif production < enemy_factory_biscuits:
    difference = enemy_factory_biscuits - production
    percentage = (difference / enemy_factory_biscuits) * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")