# class method in python


class Employee:
    company = "Apple"
    salary = "100k"

    def show(self):
        print(f"The company is {self.company} and salary is {self.salary}")

    @classmethod
    def change_data(cls, cmp, slr):
        cls.company = cmp
        cls.salary = slr


e1 = Employee()
e1.show()
e1.change_data("google", "150k")
e1.show()

print("--------------------------------")

e2 = Employee()
e2.show()
