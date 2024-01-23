from collections import deque

given_string = deque(input())
opening = deque()
balanced = True

while given_string:
    to_check = given_string.popleft()
    if to_check in "{[(":
        opening.append(to_check)
    elif not opening:
        balanced = False
        break
    else:
        if (opening.pop() + to_check) not in "{}[]()":
            balanced = False
            break

if balanced and not opening:
    print("YES")
else:
    print("NO")





