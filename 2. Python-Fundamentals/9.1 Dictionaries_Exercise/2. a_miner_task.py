my_dict = {}
material = input()
while material != "stop":
    quantity = int(input())
    if material not in my_dict:
        my_dict[material] = 0
    my_dict[material] += quantity
    material = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")