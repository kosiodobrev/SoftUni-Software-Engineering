empty_stack = []

for i in range(int(input())):
    command = [int(x) for x in input().split()]
    com_n = command[0]
    if com_n == 1:
        empty_stack.append(command[1])
    elif com_n == 2:
        if empty_stack:
            empty_stack.pop()
    elif com_n == 3:
        if empty_stack:
            print(max(empty_stack))
    elif com_n == 4:
        if empty_stack:
            print(min(empty_stack))
empty_stack.reverse()
print(*empty_stack, sep=", ")
