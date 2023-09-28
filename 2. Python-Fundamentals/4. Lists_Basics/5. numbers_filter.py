n = int(input())
my_list = []
filtered_list = []
for i in range(n):
    given_number = int(input())
    my_list.append(given_number)
command = input()
if command == "even":
    for number in my_list:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in my_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in my_list:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in my_list:
        if number >= 0:
            filtered_list.append(number)
print(filtered_list)