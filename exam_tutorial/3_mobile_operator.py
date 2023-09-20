contract_years = input()
type_of_contract = input()
mobile_internet = input()
months_for_payment = int(input())
tax = 0
total_price = 0
if contract_years == "one":
    if type_of_contract == "Small":
        tax = 9.98
    elif type_of_contract == "Middle":
        tax = 18.99
    elif type_of_contract == "Large":
        tax = 25.98
    elif type_of_contract == "ExtraLarge":
        tax = 35.99
elif contract_years == "two":
    if type_of_contract == "Small":
        tax = 8.58
    elif type_of_contract == "Middle":
        tax = 17.09
    elif type_of_contract == "Large":
        tax = 23.59
    elif type_of_contract == "ExtraLarge":
        tax = 31.79
if mobile_internet == "yes":
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
if contract_years == "two":
    tax *= 0.9625
total_price = months_for_payment * tax
print(f"{total_price:.2f} lv.")
