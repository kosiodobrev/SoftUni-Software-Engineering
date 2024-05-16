number_of_students = int(input())

students = {}

for i in range(number_of_students):
    name, grade_str = input().split()
    grade = float(grade_str)
    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

for key, value in students.items():
    avg_grade = 0
    for i in value:
        avg_grade += i
    avg_grade = avg_grade / len(value)
    value = tuple(format(x, ".2f") for x in value)
    print(f"{key} ->", *value, f"(avg: {avg_grade:.2f})")
