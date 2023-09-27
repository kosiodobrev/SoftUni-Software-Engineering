key = int(input())
n = int(input())
end_result = ""
for index in range(n):
    current_character = input()
    ascii_letter = ord(current_character)
    ascii_number = ascii_letter
    ascii_number += key
    end_result = chr(ascii_number)
    print(end_result, end="")


