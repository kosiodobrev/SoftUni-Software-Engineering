companies_dict = {}
command = input()
while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in companies_dict:
        companies_dict[company] = []
    if employee_id in companies_dict[company]:
        command = input()
        continue
    else:
        companies_dict[company].append(employee_id)
    command = input()
for key,value in companies_dict.items():
    print(f"{key}")
    for item in value:
        print(f"-- {item}")
