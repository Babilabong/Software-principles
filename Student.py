

class Student():
    def __init__(self, name, id):
        """
        this function will create a student object
        :param name: student name
        :param id: student ID
        """
        self.name = name
        self.__id = id
        self.courses = []

    def getID(self):
        """
        :return: student ID
        """
        return self.__id

    def addCourse(self, course):
        """
        this function adds a course to the student courses list if the course grade is (0-100)
        :param course: Course object
        :return: none
        """
        if course.grade >= 0 and course.grade <= 100:
            if not self.courseAlreadyExist(course.getCourseName(),course.getGrade()):
                self.courses.append(course)

    def courseAlreadyExist(self, courseName, grade):
        """
        this function checks if the course is already present in the student courses if true update is grade
        :param courseName: course name
        :param grade: course grade
        :return: bool True if the course is already present in the student courses
        """
        for course in self.courses:
            if course.getCourseName() == courseName:
                course.grade = grade
                return True
        return False

    def getCoursesList(self):
        """
        :return: courses list
        """
        return self.courses

