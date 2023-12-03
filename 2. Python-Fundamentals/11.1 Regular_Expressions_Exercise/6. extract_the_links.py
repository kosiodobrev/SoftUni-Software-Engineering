import re
pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z\.?]+)"
text = input()
while text:
    match = re.findall(pattern, text, re.IGNORECASE)
    for item in match:
        print(item)
    text = input()
