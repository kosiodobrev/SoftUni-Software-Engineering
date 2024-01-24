p = int(input())

set_1 = set()
set_2 = set()
len_counter = 0
result_intersection = []
for _ in range(p):
    set_1 = set()
    set_2 = set()
    n, m = input().split("-")
    n = [int(x) for x in n.split(",")]
    m = [int(x) for x in m.split(",")]
    for num in range(n[0], n[1] + 1):
        set_1.add(num)
    for num in range(m[0], m[1] + 1):
        set_2.add(num)
    if len(set_1.intersection(set_2)) > len_counter:
        len_counter = len(set_1.intersection(set_2))
        result_intersection = list(set_1.intersection(set_2))
print(f"Longest intersection is {result_intersection} with length {len_counter}")

