n = int(input())

matrix = []
list_to_append = []

for i in range(n):
    data = [int(x) for x in input().split(', ')]
    for j in data:
        if j % 2 == 0:
            list_to_append.append(j)
    matrix.append(list_to_append)
    list_to_append = []

print(matrix)
