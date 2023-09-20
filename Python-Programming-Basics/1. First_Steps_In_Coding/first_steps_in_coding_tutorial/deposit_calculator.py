deposit = float(input())
months = int(input())
tax = float(input()) / 100

sum = deposit + months * ((deposit * tax) / 12)
print(sum)
