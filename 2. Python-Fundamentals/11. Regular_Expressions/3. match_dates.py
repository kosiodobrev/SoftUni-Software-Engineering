import re

input_string = input()

regex = r"\(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

matches = re.findall(regex, input_string)
#print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
print(matches)