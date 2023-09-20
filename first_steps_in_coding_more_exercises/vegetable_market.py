price_kg_vegetables = float(input())
price_kg_fruits = float(input())
sum_kg_vegetables = int(input())
sum_kg_fruits = int(input())

sum_vegetables_kg = price_kg_vegetables * sum_kg_vegetables
sum_fruits_kg = price_kg_fruits * sum_kg_fruits
sum_lv = sum_vegetables_kg + sum_fruits_kg
final_sum_euro = sum_lv / 1.94

print(f"{final_sum_euro:.2f}")

