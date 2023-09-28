n = int(input())
given_word = input()
my_list = []
filtered_list = []
for current_string in range(n):
    given_string = input()
    my_list.append(given_string)
    if given_word in given_string:
        filtered_list.append(given_string)

print(my_list)
print(filtered_list)