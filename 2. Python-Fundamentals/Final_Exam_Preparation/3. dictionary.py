text = input().split(" | ")
hand_book = {}
test_word = input().split(" | ")
command = input()

for words_with_definition in text:
    word_and_definition = words_with_definition.split(": ")
    if word_and_definition[0] not in hand_book:
        hand_book[word_and_definition[0]] = []
        hand_book[word_and_definition[0]].append(word_and_definition[1])
    else:
        hand_book[word_and_definition[0]].append(word_and_definition[1])

if command == "Test":
    for current_word in test_word:
        if current_word in hand_book:
            print(f"{current_word}:")
            for item in hand_book[current_word]:
                print(f" -{item}")
        else:
            continue
elif command == "Hand Over":
    for key in hand_book:
        print(key, end=" ")