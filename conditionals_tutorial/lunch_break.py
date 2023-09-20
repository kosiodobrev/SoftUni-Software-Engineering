from math import ceil
serial_name = str(input())
duration_episode = int(input())
duration_break = int(input())

lunch_time = 1/8 * duration_break
otdih_time = 1/4 * duration_break

total_break_time_needed = duration_episode + lunch_time + otdih_time

difference = ceil(abs(duration_break - total_break_time_needed))

if total_break_time_needed <= duration_break:
    print(f"You have enough time to watch {serial_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {difference} more minutes.")