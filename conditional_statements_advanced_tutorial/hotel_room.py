month = input()
number_nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * number_nights
    apartment_price = 65 * number_nights
elif month == "June" or month == "September":
    studio_price = 75.20 * number_nights
    apartment_price = 68.70 * number_nights
elif month == "July" or month == "August":
    studio_price = 76 * number_nights
    apartment_price = 77 * number_nights

if 7 < number_nights <= 14 and (month == "May" or month == "October"):
    studio_price *= 0.95
elif number_nights > 14 and (month == "May" or month == "October"):
    studio_price *= 0.70
elif number_nights > 14 and (month == "June" or month == "September"):
    studio_price *= 0.80

if number_nights > 14:
    apartment_price *= 0.90

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
