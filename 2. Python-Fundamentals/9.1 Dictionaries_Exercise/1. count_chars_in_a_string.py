symbols = [character for character in input() if character != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters:
        letters[symbol] = 0
    letters[symbol] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")