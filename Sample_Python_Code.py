# Student Marks Calculator

def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


# Main program
name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = calculate_grade(average)

print("\n--- STUDENT REPORT ---")
print("Name:", name)
print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", average)
print("Grade:", grade)