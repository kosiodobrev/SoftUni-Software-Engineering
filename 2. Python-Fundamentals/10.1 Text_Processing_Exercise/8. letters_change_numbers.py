given_strings = [current_string.strip() for current_string in input().split()]
number = ""
letters = ""
position = 0
result = 0
counter = 0
for current_string in given_strings:
    for character in current_string:
        if character.isdigit():
            number += character
        else:
            letters += character

    number = int(number)
    for letter in letters:
        if "A" <= letter.upper() <= "Z":
            position = ord(letter.upper()) - ord("A") + 1
        if counter > 0:
            if letter.isupper():
                number = number - position
                continue
            elif letter.islower():
                number = number + position
                continue
        elif counter == 0:
            if letter.isupper():
                number = number / position
            elif letter.islower():
                number = number * position
        counter += 1

    result += number
    number = ""
    position = 0
    letters = ""
    counter = 0
print(f"{result:.2f}")


