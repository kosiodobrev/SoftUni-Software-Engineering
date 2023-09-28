n = int(input())
positive_list = []
negative_list = []
positive_counter = 0
negative_counter = 0
for i in range(n):
    current_int = int(input())
    if current_int < 0:
        negative_counter += current_int
        negative_list.append(current_int)
    else:
        positive_counter += 1
        positive_list.append(current_int)
print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {negative_counter}")