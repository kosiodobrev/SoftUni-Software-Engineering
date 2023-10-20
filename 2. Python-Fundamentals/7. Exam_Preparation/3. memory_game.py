def main():
    sequence_of_elements = input().split()
    counter_moves = 0

    while True:
        counter_moves += 1
        command = input()

        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break

        index_1, index_2 = map(int, command.split())

        if is_invalid_input(index_1, index_2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, counter_moves)
        else:
            handle_valid_input(index_1, index_2, sequence_of_elements, counter_moves)

def is_invalid_input(index1, index2, sequence):
    return (
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence)
        or index2 >= len(sequence)
    )

def handle_invalid_input(sequence, counter_moves):
    mid_index = len(sequence) // 2
    sequence.insert(mid_index, f"-{counter_moves}a")
    sequence.insert(mid_index, f"-{counter_moves}a")
    print(f"Invalid input! Adding additional elements to the board")

def handle_valid_input(index_1, index_2, sequence, counter_moves):
    if sequence[index_1] == sequence[index_2]:
        print(f"Congrats! You have found matching elements - {sequence[index_1]}!")
        second_element = sequence[index_2]
        sequence.pop(index_1)
        sequence.remove(second_element)
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {counter_moves} turns!")
        exit()

main()