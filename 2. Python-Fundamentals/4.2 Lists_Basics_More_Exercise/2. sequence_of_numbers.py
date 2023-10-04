sequence = input().split(" ")
given_string = input()
message = ""
sequence_to_int = [int(num) for num in sequence]
for i in sequence:
    summed = 0
    number = i
    for n in number:
        summed += int(n)
    while summed >= len(given_string):
        summed -= len(given_string)
    message += given_string[summed]
    given_string = given_string[0:summed] + given_string[summed + 1:]
print(message)
