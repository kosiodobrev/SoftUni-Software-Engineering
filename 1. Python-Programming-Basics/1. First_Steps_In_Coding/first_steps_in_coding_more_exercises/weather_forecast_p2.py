grad = float(input())

if 26.00 <= grad <= 35.00:
    print("Hot")
elif 20.1 <= grad <= 25.9:
    print("Warm")
elif 15.00 <= grad <= 20.00:
    print("Mild")
elif 12.00 <= grad <= 14.9:
    print("Cool")
elif 5.00 <= grad <= 11.9:
    print("Cold")
else:
    print("unknown")