x = float(input())
y = float(input())
h = float(input())

razhod_zelena_boq_litur = 3.4
razhod_chervena_boq_litur = 4.3

front_wall = (x * x) - (1.2 * 2)
back_wall = (x * x)
side_walls = ((x * y) - (1.5 * 1.5)) * 2

roof_sides = (x * y) * 2
roof_front_back = (1/2 * x * h) * 2

final_zelena_boq = (front_wall + back_wall + side_walls) / 3.4
final_chervena_boq = (roof_sides + roof_front_back) / 4.3

print(f'{final_zelena_boq: .2f}')
print(f'{final_chervena_boq: .2f}')
