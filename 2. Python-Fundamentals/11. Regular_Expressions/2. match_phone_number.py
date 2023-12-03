import re
text = input()
pattern = r"\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b"
match = re.findall(pattern, text)
print(", ".join(match))