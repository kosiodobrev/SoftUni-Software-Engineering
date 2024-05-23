from collections import deque

expression = input().split()
numbers = deque()

for char in expression:
    if char not in "*+-/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if char == "+":
                numbers.appendleft(first_number + second_number)
            elif char == "-":
                numbers.appendleft(first_number - second_number)
            elif char == "*":
                numbers.appendleft(first_number * second_number)
            elif char == "/":
                numbers.appendleft(first_number // second_number)

print(numbers[0])
