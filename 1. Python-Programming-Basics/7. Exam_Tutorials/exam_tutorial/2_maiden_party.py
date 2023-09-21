maiden_party_price = float(input())
number_love_letters = int(input())
number_wax_roses = int(input())
number_keychains = int(input())
number_caricature = int(input())
number_lucky_surprise = int(input())

price_love_letters = number_love_letters * 0.60
price_wax_roses = number_wax_roses * 7.20
price_keychains = number_keychains * 3.60
price_caricature = number_caricature * 18.20
price_lucky_surprise = number_lucky_surprise * 22

total_price = price_love_letters + price_wax_roses + price_keychains + price_caricature + price_lucky_surprise

total_items = number_love_letters + number_wax_roses + number_keychains + number_caricature + number_lucky_surprise

if total_items >= 25:
    total_price *= 0.65

final_price = total_price * 0.90
difference = abs(final_price - maiden_party_price)
if final_price >= maiden_party_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
