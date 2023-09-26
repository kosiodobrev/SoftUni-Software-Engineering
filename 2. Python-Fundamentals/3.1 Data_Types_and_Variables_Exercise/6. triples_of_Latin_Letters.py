integer = int(input())
for first_symbol in range(integer):
    for second_symbol in range(integer):
        for third_symbol in range(integer):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")
