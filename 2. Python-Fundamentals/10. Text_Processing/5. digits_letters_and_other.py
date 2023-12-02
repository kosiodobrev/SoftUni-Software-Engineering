word = input()
digits = ""
characters = ""
others = ""
for character in word:
    if character.isalpha():
        characters += character
    elif character.isdigit():
        digits += character
    else:
        others += character

print(f"{digits}")
print(f"{characters}")
print(f"{others}")