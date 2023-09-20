nailon_m2 = int(input())
boq_ltr = int(input())
razreditel = int(input())
chasove = int(input())

torbichki = 0.4
sum_materiali = ((nailon_m2 + 2) * 1.50) + \
                ((boq_ltr + (boq_ltr * 0.1)) * 14.50) + \
                (razreditel * 5) + torbichki

zaplashtane_maistori = sum_materiali * 0.3
final_sum = sum_materiali + chasove * zaplashtane_maistori
print(final_sum)