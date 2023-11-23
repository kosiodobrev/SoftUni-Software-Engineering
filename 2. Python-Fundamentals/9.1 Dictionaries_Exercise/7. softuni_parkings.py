n = int(input())
result_dict = {}
for current_person in range(n):
    command = input().split(" ")
    name = command[1]

    if command[0] == "register":
        license_plate = command[2]
        if name not in result_dict:
            result_dict[name] = ""
        else:
            print(f"ERROR: already registered with plate number {result_dict[name]}")
            continue
        result_dict[name] += license_plate
        print(f"{name} registered {license_plate} successfully")

    if command[0] == "unregister":
        if name not in result_dict:
            print(f"ERROR: user {name} not found")
        else:
            result_dict.pop(name)
            print(f"{name} unregistered successfully")

for key, value in result_dict.items():
    print(f"{key} => {value}")