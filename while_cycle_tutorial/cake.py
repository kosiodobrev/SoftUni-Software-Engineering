lenght = int(input())
width = int(input())
cake_pieces = lenght * width
while cake_pieces > 0:
    taken_pieces = input()
    if taken_pieces != "STOP":
        cake_pieces -= int(taken_pieces)
    if taken_pieces == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break
    elif cake_pieces <= 0:
        difference = abs(int(taken_pieces) - cake_pieces)
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break
