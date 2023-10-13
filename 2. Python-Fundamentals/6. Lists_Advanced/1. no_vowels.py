my_text = input()
result = [character for character in my_text if character.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(result))

