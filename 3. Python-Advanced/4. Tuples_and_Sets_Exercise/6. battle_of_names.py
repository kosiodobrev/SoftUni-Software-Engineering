n = int(input())

odd_set = set()
even_set = set()
row_counter = 0
name_value = 0

for _ in range(n):
    name = input()
    row_counter += 1
    ascii_value = 0
    for char in name:
        ascii_value += ord(char)
    name_value = ascii_value // row_counter
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(even_set) == sum(odd_set):
    print(f"{', '.join([str(x) for x in list(even_set | odd_set)])}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join([str(x) for x in list(odd_set - even_set)])}")
elif sum(even_set) > sum(odd_set):
    print(f"{', '.join([str(x) for x in list(even_set ^ odd_set)])}")
