from collections import deque
text = deque(input())
characters = {}
counter = 0
for char in sorted(text):
    counter = 0
    if char in characters:
        characters[char] += 1
        continue
    else:
        characters[char] = 0
    characters[char] += 1
for key, value in characters.items():
    print(f"{key}: {value} time/s")
