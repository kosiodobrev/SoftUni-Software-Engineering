day_target = int(input())
service_type = input()
total_sum = 0
while service_type != "closed" or total_sum != day_target:

    if service_type == "haircut":
        type_haircut = input()
        if type_haircut == "mens":
            total_sum += 15
        elif type_haircut == "ladies":
            total_sum += 20
        elif type_haircut == "kids":
            total_sum += 10
    elif service_type == "color":
        type_haircut = input()
        if type_haircut == "touch up":
            total_sum += 20
        elif type_haircut == "full color":
            total_sum += 30

    if service_type == "closed":
        break
    elif total_sum >= day_target:
        break
    service_type = input()
difference = abs(total_sum - day_target)
if total_sum >= day_target:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {difference}lv. more.")
print(f"Earned money: {total_sum}lv.")