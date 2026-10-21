def calculate_statistics(*marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    return highest, lowest, average


def calculate_grades(**subjects):
    grades = {}
    for subject, marks in subjects.items():
        if marks >= 90:
            grades[subject] = "A"
        elif marks >= 75:
            grades[subject] = "B"
        elif marks >= 60:
            grades[subject] = "C"
        elif marks >= 40:
            grades[subject] = "D"
        else:
            grades[subject] = "F"
    return grades


def display_distribution(grades):
    distribution = {}
    for grade in grades.values():
        distribution[grade] = distribution.get(grade, 0) + 1
    print("Grade Distribution:", distribution)


def main():
    marks = (85, 92, 76, 68, 45)

    maximum, minimum, average = calculate_statistics(*marks)

    print("Student Marks:", marks)
    print("Highest Marks:", maximum)
    print("Lowest Marks:", minimum)
    print(f"Average Marks: {average:.2f}")

    grades = calculate_grades(
        Python=85,
        Mathematics=92,
        Physics=76,
        English=68,
        Chemistry=45
    )

    print("\nSubject Grades:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    display_distribution(grades)


if __name__ == "__main__":
    main()
