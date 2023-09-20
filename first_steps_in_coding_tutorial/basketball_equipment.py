training_tax = int(input())
sneakers = training_tax - (training_tax * 0.40)
clothes = sneakers - (sneakers * 0.2)
ball = clothes * 0.25
gadgets = ball * 0.2

sum = training_tax + sneakers + clothes + ball + gadgets

print(f"{sum:.2f}")