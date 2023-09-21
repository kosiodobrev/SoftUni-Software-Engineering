letter = input()
output = ""
o_counter = 0
c_counter = 0
n_counter = 0
while letter != 'End':
    if letter == "n":
        n_counter += 1
    elif letter == "o":
        n_counter += 1
        if o_counter > 1:
            output += letter
    elif letter == "c":
        c_counter += 1
        if c_counter > 1:
            output += " "
    letter = input()

print(output)