number_of_lines = int(input())
opened_brackets = 0
for current_line in range(number_of_lines):
    random_input = input()
    if random_input == "(":
        opened_brackets += 1
    elif random_input == ")":
        opened_brackets -= 1
    if opened_brackets != 0 and opened_brackets != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")