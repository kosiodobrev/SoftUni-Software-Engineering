pages_per_book = int(input())
pages_per_hour = int(input())
days = int(input())

result = (pages_per_book / pages_per_hour) / days
print(int(result))
