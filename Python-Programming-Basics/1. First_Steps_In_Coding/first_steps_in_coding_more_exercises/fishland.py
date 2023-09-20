skumriq_lv_kg = float(input())
caca_lv_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi = int(input())

palamud_cena = (skumriq_lv_kg * 0.6) + skumriq_lv_kg
safrid_cena = (caca_lv_kg * 0.8) + caca_lv_kg

final_palamud = palamud_cena * palamud_kg
final_safrid = safrid_cena * safrid_kg
final_midi = midi * 7.50

final_sum = final_midi + final_safrid + final_palamud
print(f'{final_sum:.2f}')