number_kozunak = int(input())
number_pack_eggs = int(input())
cookies_kg = int(input())

eggs_dye = (number_pack_eggs * 12) * 0.15
costs = (number_kozunak * 3.20) + (number_pack_eggs * 4.35) + (cookies_kg * 5.40) + eggs_dye
print(f"{costs:.2f}")