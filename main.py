"""
created by Almog Babila
this program using Course class and Student class so make sure you have them
this program read all the database from the txt file and then you have 4 choices:
1. enter full name of student and get his Avg
2. enter full name of course and get the Avg of all student that in this course
3. enter file path and get in that file all the ID students with their Avg sort by lines
4. exit program
"""
from Course import Course
from Student import Student
from functools import reduce


def forChoice3(student):
    """
    This function printing to file the student ID and his average
    :param student: a Student object
    :return: none
    """
    grades = list(map(lambda x: x.grade, student.courses))
    average = reduce(lambda a,b:a+b,grades)/len(grades)
    file.writelines(f"{student.getID()} {average}\n")




students = []
path = input("Enter the path of the file\n")
try:
    file = open(path, "r")
    i = 0
    for line in file:
        parts = line.split('\t')
        courses = parts[2].split(';')
        stu = Student(parts[0],parts[1])
        students.append(stu)
        for courseDetails in courses:
            courseName,courseGrade = courseDetails.split('#')
            cou = Course(courseName)
            cou.setGrade(int(courseGrade))
            students[i].addCourse(cou)

        i += 1


    file.close()
except FileNotFoundError:
    print("File not found")

else:
    while(1):
        print("Enter 1 in order to calculate the average of a particular student")
        print("Enter 2 in order to calculate the average of a particular course")
        print("Enter 3 in order to calculate the average of all the students")
        print("Enter 4 in order to exit")
        choice = input("")


        if choice == '1':
            filter_students = []
            name = input("Enter the name of the student: ")
            filter_students = list(filter(lambda x: x.name == name, students))
            try:
                student = next(iter(filter_students))
            except StopIteration:
                print("student not found\n")
            else:
                grades = list(map(lambda x: x.grade, student.courses))
                average = reduce(lambda a,b:a+b,grades)/len(grades)
                print("Student ID:", student.getID())
                print("Average score:", average)
                print()


        elif choice == '2':
            name = input("Enter the name of the course: ")

            # getting all the courses to one list
            all_courses = sum(map(lambda student: student.courses, students), [])

            # filtering the course we want
            filtered_courses = list(filter(lambda course: course.course_name == name, all_courses))

            # check if the course exist and get the avg
            if filtered_courses:
                average = sum(map(lambda course: course.grade, filtered_courses)) / len(filtered_courses)
                print(f"Course {name}:")
                print(f"Average score: {average}\n")
            else:
                print(f"No courses found with the name {name}\n")


        elif choice == '3':
            path = input("Enter the path of the file:\n")
            try:
                file = open(path, "w")
                list(map(forChoice3,students))
                file.close()
            except FileNotFoundError:
                print("File not found")


        elif choice == '4':
            print("goodbye")
            break


        else:
            print("Invalid input entered")