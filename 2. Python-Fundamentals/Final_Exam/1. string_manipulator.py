given_string = input()
command = input()
prep_list = []

while command != "End":
    if "Translate" in command:
        action, char, replacement = command.split()
        given_string = given_string.replace(char, replacement)
        print(given_string)
    elif "Includes" in command:
        action, substring = command.split()
        if substring in given_string:
            print("True")
        else:
            print("False")
    elif "Start" in command:
        action, substring = command.split()
        new_given_string = given_string.split()
        if substring == new_given_string[0]:
            print("True")
        else:
            print("False")
    elif "Lowercase" in command:
        given_string = given_string.lower()
        print(given_string)
    elif "FindIndex" in command:
        action, index = command.split()
        for char in range(len(given_string) -1, -1, -1):
            if given_string[char].lower() == index:
                print(char)
                break
    elif "Remove" in command:
        action, start_index, count = command.split()
        start_index = int(start_index)
        count = int(count)
        first = given_string[:start_index]
        second = given_string[count + start_index:]
        new_string = first + second
        print(new_string)

    command = input()