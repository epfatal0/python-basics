def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def print_summary(student_list):
    print("Student Summary:")
    for student in student_list:
        name = student[0]
        score = student[1]
        grade = student[2]
        print(f"{name}: {score} -> {grade}")

def save_to_file(student_list):
    with open("grades.txt", "w") as file:
        for student in student_list:
            name = student[0]
            score = student[1]
            grade = student[2]
            file.write(f"{name}: {score} -> {grade}\n")

print("Welcome to the Student Grade Tracker!\n")

students = []

while True:
    name = input("Enter your first and last name: ").title()
    score = int(input("Enter score (0 - 100): "))

    if score < 0 or score > 100:
        print("Try again. Enter a score between 0 - 100.")
        continue

    grade = get_letter_grade(score)
    student = (name, score, grade)
    students.append(student)

    another_student = input("\nAdd another student? (Yes / No:) ").lower()
    if another_student == "yes" or another_student == "y":
        continue

    elif another_student == "no" or another_student == "n":
        break
    else:
        print("Try again. Please enter Yes or No.")
    
print()
print_summary(students)
save_to_file(students)
print("\nData saved")