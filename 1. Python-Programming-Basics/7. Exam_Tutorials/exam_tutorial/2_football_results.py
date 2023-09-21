result_football_match1 = str(input())
result_football_match2 = str(input())
result_football_match3 = str(input())

scores1 = result_football_match1.split(":")
scores2 = result_football_match2.split(":")
scores3 = result_football_match3.split(":")

number_wins = 0
number_loses = 0
number_draws = 0

team1_scores1 = int(scores1[0])
team2_scores1 = int(scores1[1])

team1_scores2 = int(scores2[0])
team2_scores2 = int(scores2[1])

team1_scores3 = int(scores3[0])
team2_scores3 = int(scores3[1])

# Check if the first team won the match
if team1_scores1 > team2_scores1:
    number_wins += 1
elif team1_scores1 < team2_scores1:
    number_loses += 1
else:
    number_draws += 1

if team1_scores2 > team2_scores2:
    number_wins += 1
elif team1_scores2 < team2_scores2:
    number_loses += 1
else:
    number_draws += 1

if team1_scores3 > team2_scores3:
    number_wins += 1
elif team1_scores3 < team2_scores3:
    number_loses += 1
else:
    number_draws += 1

print(f"Team won {number_wins} games.")
print(f"Team lost {number_loses} games.")
print(f"Drawn games: {number_draws}")