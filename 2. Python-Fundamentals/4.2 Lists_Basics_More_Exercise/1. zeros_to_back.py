given_string = input().split(", ")
convert_to_int = [int(num) for num in given_string]
counter = 0
for i in convert_to_int:
    if i == 0:
        convert_to_int.remove(i)
        convert_to_int.append(i)
print(convert_to_int)