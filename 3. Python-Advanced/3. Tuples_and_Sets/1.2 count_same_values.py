numbers = tuple([float(x) for x in input().split()])

occ = {}

for num in numbers:
    occ[num] = numbers.count(num)

for key, value in occ.items():
    print(f"{key:.1f} - {value} times")
