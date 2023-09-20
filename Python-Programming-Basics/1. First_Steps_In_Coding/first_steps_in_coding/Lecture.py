result_football_match1 = str(input())
result_football_match2 = str(input())
result_football_match3 = str(input())

scores1 = result_football_match1.split(":")
scores2 = result_football_match2.split(":")
scores3 = result_football_match3
# Extract the scores for each team
team1_score1 = int(scores1[0])
team2_score1 = int(scores1[1])
# Check if the first team won the match
if team1_score > team2_score:
    print("The team won the match!")
elif team1_score < team2_score:
    print("The team lost the match.")
else:
    print("It was a draw.")
