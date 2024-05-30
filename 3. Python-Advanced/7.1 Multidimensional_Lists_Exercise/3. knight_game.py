n = int(input())

matrix = []
knights = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1),(1, -2), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
