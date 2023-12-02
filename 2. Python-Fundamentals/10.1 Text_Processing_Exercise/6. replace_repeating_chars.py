given_string = input()
result_string = ""
last_added_character = ""
for current_character in given_string:
    if current_character != last_added_character:
        last_added_character = current_character
        result_string += last_added_character
print(result_string)