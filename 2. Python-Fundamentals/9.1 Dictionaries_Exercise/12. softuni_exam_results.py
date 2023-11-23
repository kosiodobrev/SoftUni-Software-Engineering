results_dict = {}
submissions_dict = {}
command = input()
while command != "exam finished":
    if "banned" in command:
        username, status = command.split("-")
        results_dict.pop(username)
        command = input()
        continue

    username, language, points = command.split("-")

    points = int(points)
    if points > 100:
        points = 100

    if username not in results_dict:
        results_dict[username] = []
    results_dict[username].append(points)

    if language not in submissions_dict:
        submissions_dict[language] = 0
    submissions_dict[language] += 1

    command = input()

print("Results:")
for key, value in results_dict.items():
    print(f"{key} | {max(value)}")
print("Submissions:")
for key, value in submissions_dict.items():
    print(f"{key} - {value}")