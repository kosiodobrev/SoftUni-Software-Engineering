number_students = int(input())
top_students_counter = 0               #>5.00
between_four_and_five_counter = 0      #Between 4.00 and 4.99
between_three_and_four_counter = 0     #Between 3.00 and 3.99
failed_students_counter = 0            #<3.00
average_counter = 0
all_grades_counter = 0
for current_students in range(1, number_students + 1):
    grade = float(input())
    all_grades_counter += grade
    if grade >= 5.00:
        top_students_counter += 1

    elif 4.00 <= grade <= 4.99:
        between_four_and_five_counter += 1

    elif 3.00 <= grade <= 3.99:
        between_three_and_four_counter += 1

    elif grade < 3:
        failed_students_counter += 1

average_counter = all_grades_counter / number_students
percent_top_students = top_students_counter / number_students * 100
percent_between_four_and_five = between_four_and_five_counter / number_students * 100
percent_between_three_and_four = between_three_and_four_counter / number_students * 100
percent_failed_students = failed_students_counter / number_students * 100
print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_four_and_five:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_three_and_four:.2f}%")
print(f"Fail: {percent_failed_students:.2f}%")
print(f"Average: {average_counter:.2f}")
