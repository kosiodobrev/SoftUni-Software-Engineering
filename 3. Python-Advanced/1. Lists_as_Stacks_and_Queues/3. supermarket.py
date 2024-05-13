from collections import deque

command = input()
queue = deque([])

while command != "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")