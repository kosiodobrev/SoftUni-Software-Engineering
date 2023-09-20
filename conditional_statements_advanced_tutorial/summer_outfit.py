grad = int(input())
day_time = input()
outfit = ""
shoes = ""
if day_time == "Morning":
    if 10 <= grad <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 18 < grad <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if grad >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if 10 <= grad <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < grad <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    if grad >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif day_time == "Evening":
    if 10 <= grad <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < grad <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if grad >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {grad} degrees, get your {outfit} and {shoes}.")


