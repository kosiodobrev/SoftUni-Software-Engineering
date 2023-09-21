day = int(input())
hours_for_day = int(input())
tax = 0
total_tax = 0
for day_count in range(1, day + 1):
    daily_tax = 0
    for hour_count in range(1, hours_for_day + 1):
        if day_count % 2 != 0 and hour_count % 2 == 0:
            daily_tax += 1.25
        elif day_count % 2 == 0 and hour_count % 2 != 0:
            daily_tax += 2.50
        elif day_count % 2 != 0 and hour_count % 2 != 0:
            daily_tax += 1
        elif day_count % 2 == 0 and hour_count % 2 == 0:
            daily_tax += 1
    total_tax += daily_tax
    print(f"Day: {day_count} - {daily_tax:.2f} leva")
print(f"Total: {total_tax:.2f} leva")
