#name = input()

#while name != 'End':
    #print("hello", name)
    #name = input()

#a = 0
#while a < 6:
    #a += 1
    #if a % 2 != 0:  #принтира само четни числа
        #continue
    #print(a)

#a = 0
#while a < 6:
    #a += 1
    #if a % 2 == 0:  #принтира само нечетни числа
        #continue
    #print(a)

#a = 5
#while True:
    #if a > 10:
        #break
    #print("a = " + str(a))
    #a += 1

while True:
    username = input()
    if username == "Stop":
        break
    print("Hello, ", username)
