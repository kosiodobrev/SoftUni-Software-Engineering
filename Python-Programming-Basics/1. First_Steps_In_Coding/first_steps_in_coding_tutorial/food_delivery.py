chicken_menu_n = int(input())
fish_menu_n = int(input())
vegan_menu_n = int(input())

sum_food = (chicken_menu_n * 10.35) + (fish_menu_n * 12.40) + (vegan_menu_n * 8.15)

dessert = sum_food * 0.2
delivery = 2.50
sum_order = sum_food + dessert + delivery
print(sum_order)
