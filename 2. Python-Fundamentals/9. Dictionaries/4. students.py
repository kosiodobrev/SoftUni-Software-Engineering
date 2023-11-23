students = []

course = ""

while True:
    current_student = input()

    if ":" not in current_student:
        course = current_student
        break

    name, ID, taken_course = current_student.split(":")
    students.append({"name": name, "ID": ID, "course": taken_course})

for student in students:
    if course.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")


