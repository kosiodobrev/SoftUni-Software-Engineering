sequence = [int(x) for x in input().split(" ")]
average = sum(sequence) / len(sequence)
result_list = []

for number in sequence:
    if number > average:
        result_list.append(number)

result_list.sort(reverse=True)

if len(result_list) > 0:
    print(" ".join(str(x) for x in result_list[:5]))
else:
    print("No")

