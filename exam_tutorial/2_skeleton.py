minutes_control = int(input())
seconds_control = int(input())
lenght_ulei = float(input())
seconds_100m = int(input())

minutes_to_seconds_control = minutes_control * 60
control_in_seconds = minutes_to_seconds_control + seconds_control
cut_seconds = lenght_ulei / 120 * 2.5
marin_time = (lenght_ulei / 100) * seconds_100m - cut_seconds

difference = abs(control_in_seconds - marin_time)

if marin_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")