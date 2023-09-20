sold_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
for _ in range(sold_games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fornite_counter += 1
    elif game_name == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1
percent_hearthstone = hearthstone_counter / sold_games * 100
percent_fornite = fornite_counter / sold_games * 100
percent_overwatch = overwatch_counter / sold_games * 100
percent_others = others_counter / sold_games * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
