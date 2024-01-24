n = int(input())
chemicals = set()
for i in range(n):
    compounds = input().split()
    for el in compounds:
        chemicals.add(el)
for item in chemicals:
    print(item)
