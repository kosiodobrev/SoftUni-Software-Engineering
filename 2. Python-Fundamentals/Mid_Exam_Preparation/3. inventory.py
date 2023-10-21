journal = input().split(", ")

while True:

    command = input().split(' - ')

    if command[0] == "Craft!":
        print(', '.join(journal))
        break

    if command[0] == "Collect":
        if command[1] not in journal:
            journal.append(command[1])

    if command[0] == "Drop":
        if command[1] in journal:
            journal.remove(command[1])

    if command[0] == "Combine Items":
        items_for_combo = command[1].split(":")
        if items_for_combo[0] in journal:
            index = journal.index(items_for_combo[0])
            journal.insert(index + 1, items_for_combo[1])

    if command[0] == "Renew":
        if command[1] in journal:
            journal.remove(command[1])
            journal.append(command[1])



