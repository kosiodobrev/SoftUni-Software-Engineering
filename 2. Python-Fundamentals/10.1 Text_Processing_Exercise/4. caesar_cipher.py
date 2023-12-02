text = input()
result = ""
for char in text:
    result += chr(ord(char) + 3)
print(result)