courses_dict = {}
command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)
    command = input()
for key,value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for item in value:
        print(f"-- {item}")