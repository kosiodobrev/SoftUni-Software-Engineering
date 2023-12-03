import re

numbers = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
match = re.finditer(pattern, numbers)

for matched in match:
    print(matched.group(), end=" ")