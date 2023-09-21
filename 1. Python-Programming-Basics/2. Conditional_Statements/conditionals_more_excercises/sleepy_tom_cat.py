off_days = int(input())

year_days = 365
working_days = year_days - off_days
working_days_play_time = 63 * working_days
off_days_play_time = 127 * off_days
total_play_time = working_days_play_time + off_days_play_time
needed_play_time = 30000
difference = abs(total_play_time - needed_play_time)
play_time_hours = difference // 60
play_time_minutes = difference % 60
if total_play_time > needed_play_time:
    print("Tom will run away")
    print(f"{play_time_hours} hours and {play_time_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{play_time_hours} hours and {play_time_minutes} minutes less for play")
