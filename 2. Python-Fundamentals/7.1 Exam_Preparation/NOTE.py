n = int(input())
m = int(input())
s = int(input())
for current_address in range(m, n - 1, -1):
                if current_address % 2 == 0 and current_address % 3 == 0:
                    if current_address == s:
                        break
                    else:
                        print(current_address, end=" ")

