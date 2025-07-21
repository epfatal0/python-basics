#Define function to convert score into a letter grade
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

#Define function to print all student records
def print_summary(student_list):
    print("Student Summary:")

#Go through each student and pull out name, score, and grade
    for name, score, grade in student_list:
        print(f"{name}: {score} -> {grade}")

#Define function to save student records to text file
def save_to_file(student_list):
    with open("grades.txt", "w") as file:
        for name, score, grade in student_list:
            file.write(f"{name}: {score} -> {grade}\n")

#Welcome message
print("Welcome to the Student Grade Tracker!\n")

#empty students list to store student records
students = []

#Main Program Loop

while True:
    name = input("Enter your first and last name: ").title()
    score = int(input("Enter score (0 - 100): "))

    if score < 0 or score > 100:
        print("Try again. Enter a score between 0 - 100.")
        continue

#Call function to get the letter grade based on the score / add student record to end of the list
    grade = get_letter_grade(score)
    students.append((name, score, grade))

#ask user if they want to enter another student
    another_student = input("\nAdd another student? (Yes / No:) ").lower()
    if another_student == "yes" or another_student == "y":
        continue

    elif another_student == "no" or another_student == "n":
        break
    else:
        print("Try again. Please enter Yes or No.")
    
print()
print_summary(students) #Call print_summary function to display all students
save_to_file(students) #save student records to grades.txt
print("\nData saved to grades.txt")