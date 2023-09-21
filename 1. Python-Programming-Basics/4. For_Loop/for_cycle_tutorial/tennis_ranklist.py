from math import floor
number_of_tournaments = int(input())
start_points = int(input())
total_points = 0
tournaments_won = 0
for tournament in range(number_of_tournaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        tournaments_won += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average_points = floor(total_points // number_of_tournaments)
total_points += start_points
percent_of_won_tournaments = tournaments_won / number_of_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_of_won_tournaments:.2f}%")