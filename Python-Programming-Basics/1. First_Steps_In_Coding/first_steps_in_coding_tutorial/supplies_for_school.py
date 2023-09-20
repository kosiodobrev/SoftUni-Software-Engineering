pen_packs = int(input())
marker_packs = int(input())
lr = int(input())
discount = float(input()) / 100

sum = ((pen_packs * 5.80) + (marker_packs * 7.20) + (lr * 1.20))
final_sum = sum - (sum * discount)
print(final_sum)

