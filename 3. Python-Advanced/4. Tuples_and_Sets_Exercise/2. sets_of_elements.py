n, m = input().split()

set_1 = set()
set_2 = set()

for _ in range(int(n)):
    number = input()
    set_1.add(number)
for _ in range(int(m)):
    number = input()
    set_2.add(number)

for number in set_1.intersection(set_2):
    print(number)
