list_of_numbers = input().split()
n = int(input())
from_string_to_integers = [int(number) for number in list_of_numbers]
for i in range(n):
    from_string_to_integers.remove(min(from_string_to_integers))
print(", ".join(map(str, from_string_to_integers)))
