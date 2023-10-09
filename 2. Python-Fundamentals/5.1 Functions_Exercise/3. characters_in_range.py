def all_the_characters(first_character: str, second_character: str) -> list:
    character = []
    for current_character in range(ord(first_character) + 1, ord(second_character)):
        character.append(chr(current_character))
    return character

first_char = input()
second_char = input()
final_result = all_the_characters(first_char, second_char)
print(" ".join(final_result))