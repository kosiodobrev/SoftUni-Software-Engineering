n = int(input())

student_grades = {}
avg_grade = 0

for _ in range(n):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for key, value in student_grades.items():
    avg_grade = 0
    for i in value:
        avg_grade += i
    avg_grade = avg_grade / len(value)
    f_all_grades = tuple([format(x, ".2f") for x in value])
    print(f"{key} ->", *f_all_grades, f"(avg: {avg_grade:.2f})")
