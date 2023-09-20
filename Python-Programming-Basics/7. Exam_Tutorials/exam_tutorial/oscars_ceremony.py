rent_haal = int(input())

statues = rent_haal * 0.7
catering = statues * 0.85
sound = 1/2 * catering
costs = rent_haal + statues + catering + sound
print(f"{costs:.2f}")