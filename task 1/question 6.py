def analyze(students_grades):

    count = 0
    grades = [float(grade) for grade in students_grades.split(',')]
    for grade in grades:
        if grade >= 85:
            count += 1
    return count


print("the number of the grades that bigger than 85 is: ", analyze(input("enter the grades with just( , characters) between them: ")))


