hours = int(input())
minutes = int(input())
minutes += 15           #прибавяме 15 минути
hours += minutes // 60  #проверяваме дали минутите са над 60
minutes %= 60           #ако минутите са над 60, тук пишем остатъка от добавения час
if hours > 23:
    hours = 0
print(f"{hours}:{minutes:02d}")
