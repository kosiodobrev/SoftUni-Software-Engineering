string = input()
string_list = string.split(",")     
sheep_count = 0
current_item = ""
for item in string_list[::-1]:
    if (item == " wolf" or item == "wolf") and sheep_count == 0:
        print(f"Please go away and stop eating my sheep")
        break
    elif item == " sheep":
        sheep_count += 1
    elif item == "wolf" or item == " wolf":
        print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
        break