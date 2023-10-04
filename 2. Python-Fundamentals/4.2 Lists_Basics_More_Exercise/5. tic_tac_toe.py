line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")
player = ""
line_1_int = [int(x) for x in line_1]
line_2_int = [int(y) for y in line_2]
line_3_int = [int(z) for z in line_3]

if line_1_int[0] == 1 and line_1_int[1] == 1 and line_1_int[2] == 1:
    player = "first player"
elif line_2_int[0] == 1 and line_2_int[1] == 1 and line_2_int[2] == 1:
    player = "first player"
elif line_3_int[0] == 1 and line_3_int[1] == 1 and line_3_int[2] == 1:
    player = "first player"
elif line_1_int[0] == 1 and line_2_int[0] == 1 and line_3_int[0] == 1:
    player = "first player"
elif line_1_int[1] == 1 and line_2_int[1] == 1 and line_3_int[1] == 1:
    player = "first player"
elif line_1_int[2] == 1 and line_2_int[2] == 1 and line_3_int[2] == 1:
    player = "first player"
elif line_1_int[0] == 1 and line_2_int[1] == 1 and line_3_int[2] == 1:
    player = "first player"
elif line_1_int[2] == 1 and line_2_int[1] == 1 and line_3_int[0] == 1:
    player = "first player"

elif line_1_int[0] == 2 and line_1_int[1] == 2 and line_1_int[2] == 2:
    player = "second player"
elif line_2_int[0] == 2 and line_2_int[1] == 2 and line_2_int[2] == 2:
    player = "second player"
elif line_3_int[0] == 2 and line_3_int[1] == 2 and line_3_int[2] == 2:
    player = "second player"
elif line_1_int[0] == 2 and line_2_int[0] == 2 and line_3_int[0] == 2:
    player = "second player"
elif line_1_int[1] == 2 and line_2_int[1] == 2 and line_3_int[1] == 2:
    player = "second player"
elif line_1_int[2] == 2 and line_2_int[2] == 2 and line_3_int[2] == 2:
    player = "second player"
elif line_1_int[0] == 2 and line_2_int[1] == 2 and line_3_int[2] == 2:
    player = "second player"
elif line_1_int[2] == 2 and line_2_int[1] == 2 and line_3_int[0] == 2:
    player = "second player"
else:
    player = "draw"

if player == "first player":
    print("First player won")
elif player == "second player":
    print("Second player won")
else:
    print("Draw!")
