n = int(input())

usernames = set()

for _ in range(n):
    username = input()
    if username not in usernames:
        usernames.add(username)

for username in usernames:
    print(username)
