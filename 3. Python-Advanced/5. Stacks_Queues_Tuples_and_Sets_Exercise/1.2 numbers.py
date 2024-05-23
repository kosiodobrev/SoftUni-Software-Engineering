first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

numbers = []

for _ in range(int(input())):
    command = input().split()
    for i in command:
        if i.isdigit():
            numbers.append(int(i))
    operation = command[0]
    which_seq = command[1]
    if operation == "Add":
        if which_seq == "First":
            for number in numbers:
                first_seq.add(number)
        elif which_seq == "Second":
            for number in numbers:
                second_seq.add(number)
    elif operation == "Remove":
        if which_seq == "First":
            for number in numbers:
                if number in first_seq:
                    first_seq.remove(number)
        elif which_seq == "Second":
            for number in numbers:
                if number in second_seq:
                    second_seq.remove(number)
    elif operation == "Check" and which_seq == "Subset":
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print(True)
        else:
            print(False)
    numbers = []

first_seq = sorted(first_seq)
second_seq = sorted(second_seq)

print(*first_seq, sep=", ")
print(*second_seq, sep=", ")


