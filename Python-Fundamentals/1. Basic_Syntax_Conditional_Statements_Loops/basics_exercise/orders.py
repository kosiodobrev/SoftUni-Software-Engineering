number_of_orders = int(input())
total_price = 0
for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100.00:
        if 1 <= days <= 31:
            if 1 <= capsules_per_day <= 2000:
                order_price = price_per_capsule * capsules_per_day * days
                total_price += order_price
                print(f"The price for the coffee is: ${order_price:.2f}")
            else:
                continue
        else:
            continue
    else:
        continue
print(f"Total: ${total_price:.2f}")

