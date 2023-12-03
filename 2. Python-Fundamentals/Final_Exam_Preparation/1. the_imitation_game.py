encrypted_message = input()
command = input()

while command != "Decode":
    new_command = command.split("|")

    if "Move" in command:
        cmd, number = command.split("|")
        number = int(number)
        encrypted_message = encrypted_message[number:] + encrypted_message[:number]
    elif "Insert" in command:
        cmd, index, value = command.split("|")
        index = int(index)
        first = encrypted_message[:index]
        second = encrypted_message[index:]
        encrypted_message = first + value + second
    elif "ChangeAll" in command:
        cmd, substring, replacement = command.split("|")
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")


