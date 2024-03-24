class Course():
    def __init__(self,course_name):
        """
        this function will create a course with grade 101
        :param course_name: the name of the course
        """
        self.course_name = course_name
        self.grade = 101

    def setGrade(self,grade):
        """
        this function will set the grade value
        :param grade: grade value
        :return: none
        """
        if grade >= 0 and grade <= 100:
            self.grade = grade

    def getGrade(self):
        """
        :return: grade
        """
        return self.grade

    def getCourseName(self):
        """
        :return: course name
        """
        return self.course_name