number_messages = int(input())

for i in range(number_messages):
    message = int(input())
    if message == 88:
        message = "Hello"
    elif message == 86:
        message = "How are you?"
    elif message < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)