type_of_movie = input()
rows = int(input())
columns = int(input())
total_places = rows * columns
ticket_price = 0
if type_of_movie == "Premiere":
    ticket_price += 12
elif type_of_movie == "Normal":
    ticket_price += 7.5
elif type_of_movie == "Discount":
    ticket_price += 5
total_income = ticket_price * total_places
print(f"{total_income:.2f} leva")