day_of_week = input()
ticket_price = 0

if day_of_week == "Monday":
    ticket_price += 12
    print(f"{ticket_price}")
elif day_of_week == "Tuesday":
    ticket_price += 12
    print(f"{ticket_price}")
elif day_of_week == "Wednesday":
    ticket_price += 14
    print(f"{ticket_price}")
elif day_of_week == "Thursday":
    ticket_price += 14
    print(f"{ticket_price}")
elif day_of_week == "Friday":
    ticket_price += 12
    print(f"{ticket_price}")
elif day_of_week == "Saturday":
    ticket_price += 16
    print(f"{ticket_price}")
elif day_of_week == "Sunday":
    ticket_price += 16
    print(f"{ticket_price}")
