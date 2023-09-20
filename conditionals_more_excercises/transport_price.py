n_km = int(input())
day_night = str(input())

taxi = 0
if day_night == "day":
    taxi = 0.70 + 0.79 * n_km
elif day_night == "night":
    taxi = 0.70 + 0.90 * n_km

bus = 0
if n_km >= 20:
    bus = 0.09 * n_km

train = 0
if n_km >= 100:
    train = 0.06 * n_km

if n_km < 20:
    print(f"{taxi:.2f}")
elif 20 <= n_km < 100:
    print(f"{bus:.2f}")
else:
    print(f"{train:.2f}")
