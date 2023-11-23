synonym_dict = {}
count_of_words = int(input())
for current in range(count_of_words):
    synonym_list = []
    given_word = input()
    if given_word not in synonym_dict:
        synonym_dict[given_word] = []
    synonym_word = input()
    synonym_dict[given_word].append(synonym_word)

for key in synonym_dict:
    print(f"{key} - {', '.join(synonym_dict[key])}")