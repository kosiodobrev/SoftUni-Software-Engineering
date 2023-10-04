given_list = input().split(" ")
k = int(input())
new_list = []
index_counter = 0
while len(given_list) > 0:
    for item in given_list:
        index_counter += 1
        if index_counter % 3 == 0 and index_counter != 0:
            new_list.append(item)
            given_list.remove(item)





print(new_list)