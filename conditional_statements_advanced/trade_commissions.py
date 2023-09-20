city = input()
volume_sales = float(input())

commission_prozent = 0

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        commission_prozent += 5
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 500 <= volume_sales <= 1000:
        commission_prozent += 7
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 1000 <= volume_sales <= 10000:
        commission_prozent += 8
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif volume_sales > 10000:
        commission_prozent += 12
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= volume_sales <= 500:
        commission_prozent += 4.5
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 500 <= volume_sales <= 1000:
        commission_prozent += 7.5
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 1000 <= volume_sales <= 10000:
        commission_prozent += 10
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif volume_sales > 10000:
        commission_prozent += 13
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        commission_prozent += 5.5
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 500 <= volume_sales <= 1000:
        commission_prozent += 8
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif 1000 <= volume_sales <= 10000:
        commission_prozent += 12
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    elif volume_sales > 10000:
        commission_prozent += 14.5
        commission = volume_sales * (commission_prozent / 100)
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")