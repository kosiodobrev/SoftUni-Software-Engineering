sequence = input().split(" ")
time_per_racer = len(sequence) // 2
left_racer_list = sequence[0:time_per_racer]
right_racer_list = sequence[time_per_racer + 1:]
left_racer_list_int = [int(x) for x in left_racer_list]
right_racer_list_int = [int(y) for y in right_racer_list]
left_racer_time = 0
right_racer_time = 0
winner = ""
winner_time = 0

for left_racer in left_racer_list_int:
    if left_racer == 0:
        left_racer_time *= 0.8
    else:
        left_racer_time += left_racer

for right_racer in reversed(right_racer_list_int):
    if right_racer == 0:
        right_racer_time *= 0.8
    else:
        right_racer_time += right_racer

if left_racer_time < right_racer_time:
    winner = "left"
    winner_time = left_racer_time
elif right_racer_time < left_racer_time:
    winner = "right"
    winner_time = right_racer_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")