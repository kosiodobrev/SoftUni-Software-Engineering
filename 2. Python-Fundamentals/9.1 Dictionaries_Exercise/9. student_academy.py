n = int(input())
students_dict = {}
for current_student in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(grade)
for key,value in students_dict.items():
    sum_grades = 0
    average_grade = 0
    for current_grade in value:
        sum_grades += current_grade
        average_grade = sum_grades / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")