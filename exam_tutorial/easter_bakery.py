price_brashno_kg = float(input())
brashno_kg = float(input())
sugar_kg = float(input())
eggs_pack = int(input())
maq_pack = int(input())

price_sugar_kg = price_brashno_kg * 0.75
price_eggs_pack = price_brashno_kg * 1.1
price_maq_pack = price_sugar_kg * 0.2
brashno = price_brashno_kg * brashno_kg
sugar = price_sugar_kg * sugar_kg
eggs = price_eggs_pack * eggs_pack
maq = price_maq_pack * maq_pack
final_costs = brashno + sugar + eggs + maq
print(f"{final_costs:.2f}")