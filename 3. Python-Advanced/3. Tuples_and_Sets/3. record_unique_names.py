n = int(input())

names = {}

for _ in range(n):
    name = input()
    if name not in names:
        names[name] = 0
for key, value in names.items():
    print(key)
 
