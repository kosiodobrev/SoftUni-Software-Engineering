data = input().split()

item_dict = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    item_dict[key] = value

searched_item = input().split()
for item in searched_item:
    if item in item_dict.keys():
        print(f"We have {item_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")