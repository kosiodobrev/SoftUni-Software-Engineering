year = int(input())
year_is_special = False
while not year_is_special:
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for digit in str(year):
        if year_as_string.count(digit) != 1:
            year_is_special = False
            break
print(year)
