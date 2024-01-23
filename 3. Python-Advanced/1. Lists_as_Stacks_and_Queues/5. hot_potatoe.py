from collections import deque

names = deque(input().split())
n = int(input())
result = deque()
while len(names) > 1:
    names.rotate(-n + 1)
    current_kid = names.popleft()
    print(f"Removed {current_kid}")
print(f"Last is {names[0]}")
