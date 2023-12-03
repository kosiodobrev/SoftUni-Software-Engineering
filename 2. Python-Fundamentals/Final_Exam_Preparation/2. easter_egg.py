import re

text = input()
pattern = r"[?:#@]+([a-z]{3,})[^\w+]+\/+(\d+)\/+"
match = re.findall(pattern, text)
for item in match:
    item = list(item)
    print(f"You found {item[1]} {item[0]} eggs!")