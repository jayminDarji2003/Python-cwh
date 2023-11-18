# Instance variable and Class variable


class college:
    # class variable
    college_name = "KIRC"
    no_of_teachers = 20
    courses = ["BCA", "BBA", "MCA", "MBA"]

    def __init__(self, teach, stu):
        # instance variable
        self.teacher = teach
        self.student = stu

    def showInstData(self):
        print(f"The Teacher name is : {self.teacher}")
        print(f"The Student name is : {self.student}")

    @classmethod
    def showClsData(c):
        print(f"The name of the college is : {c.college_name}")
        print(f"The no of teachers in college is : {c.no_of_teachers}")
        print(f"The cources in college is : {c.courses}")


c1 = college("Alpa mam", "harry panchal")
c1.showInstData()
print("-----------------------")
print("-----------------------")
college.showClsData()
