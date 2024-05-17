n_first_set, m_second_set = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(n_first_set):
    number = int(input())
    first_set.add(number)

for _ in range(m_second_set):
    number = int(input())
    second_set.add(number)

result = first_set.intersection(second_set)
print(*result, sep="\n")

