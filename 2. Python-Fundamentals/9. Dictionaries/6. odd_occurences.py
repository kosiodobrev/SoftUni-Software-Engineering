sequence = input().split(" ")
result_dict = {}
for word in sequence:
    word_lower = word.lower()
    if word_lower not in result_dict:
        result_dict[word_lower] = 0
    result_dict[word_lower] += 1

for key, value in result_dict.items():
    if value % 2 != 0:
        print(key, end=" ")