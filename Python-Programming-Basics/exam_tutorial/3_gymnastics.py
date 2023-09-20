country = input()
sport_equipment = input()
grade = 0
if sport_equipment == "ribbon":
    if country == "Russia":
        grade = 9.1 + 9.4
    elif country == "Bulgaria":
        grade = 9.6 + 9.4
    elif country == "Italy":
        grade = 9.2 + 9.5
elif sport_equipment == "hoop":
    if country == "Russia":
        grade = 9.3 + 9.8
    elif country == "Bulgaria":
        grade = 9.55 + 9.75
    elif country == "Italy":
        grade = 9.45 + 9.35
elif sport_equipment == "rope":
    if country == "Russia":
        grade = 9.6 + 9.0
    elif country == "Bulgaria":
        grade = 9.5 + 9.4
    elif country == "Italy":
        grade = 9.7 + 9.15
percent_max_points = ((20 - grade) / 20) * 100
print(f"The team of {country} get {grade:.3f} on {sport_equipment}.")
print(f"{percent_max_points:.2f}%")
