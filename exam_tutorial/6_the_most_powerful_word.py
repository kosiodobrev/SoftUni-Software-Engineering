import sys
from sys import maxsize
word = input()
ascii_sum = 0
word_value_counter = -sys.maxsize
while word != "End of words":
    for index, letter in enumerate(word):
        ascii_value = ord(letter)
        ascii_sum += ascii_value
        first_letter = word[0]
    if first_letter.lower() == "a" or first_letter.lower() == "e" or first_letter.lower() == "i" or first_letter.lower() == "o" or first_letter.lower() == "u" or first_letter.lower() == "y":
        ascii_sum *= len(word)
    else:
        ascii_sum //= len(word)
    if ascii_sum >= word_value_counter:
        word_value_counter = ascii_sum
        last_word = word
    ascii_sum = 0
    word = input()
print(f"The most powerful word is {last_word} - {word_value_counter}")