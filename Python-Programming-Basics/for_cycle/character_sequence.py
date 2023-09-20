#text = input()
#for i in range(len(text)):
    #print(text[i])

text = input()
ascii_sum = 0
for letter in text:
    ascii_value = ord(letter)
    ascii_sum += ascii_value
    print(letter)
    print(ascii_sum)