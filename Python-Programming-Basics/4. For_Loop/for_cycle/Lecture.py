upper_limit_1 = int(input())
upper_limit_2 = int(input())
upper_limit_3 = int(input())

pins = []

for digit1 in range(2, upper_limit_1 + 1, 2):
    for digit2 in range(2, upper_limit_2 + 1):
        if digit2 in [2, 3, 5, 7]:
            for digit3 in range(2, upper_limit_3 + 1, 2):
                pin = str(digit1) + str(digit2) + str(digit3)
                pins.append(pin)

print(pins)