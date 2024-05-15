from collections import deque
sequence = deque(input())
opening_brackets = "([{"
closing_brackets = ")]}"
counter = 0

while sequence and counter < len(sequence) / 2:
    if sequence[0] not in opening_brackets:
        break
    index = opening_brackets.index(sequence[0])
    if sequence[1] == closing_brackets[index]:
        sequence.popleft()
        sequence.popleft()
        sequence.rotate(counter)
        counter = 0
    else:
        sequence.rotate(-1)
        counter += 1

if sequence:
    print("NO")
else:
    print("YES")
