def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False



numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))