word = input()

try:
    n = int(input())
except TypeError as ex:
    print('Variable times must be an integer')
else:
    print(word*n)
