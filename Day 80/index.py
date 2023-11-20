# Multilevel inheritance


class GrandParents:
    def __init__(self):
        self.grandFather = "Bhogilal"
        self.grandMother = "Daiben"

    def show_grand_info(self):
        print(f"Grand Father name is : {self.grandFather}")
        print(f"Grand Mother name is : {self.grandMother}")
        print("--------------------------------")


class Parents(GrandParents):
    def __init__(self):
        super().__init__()
        self.father = "Satishkumar"
        self.mother = "Naynaben"

    def show_parent_info(self):
        print(f"Father name is : {self.father}")
        print(f"Mother name is : {self.mother}")
        print("--------------------------------")


class Children(Parents):
    def __init__(self):
        super().__init__()
        self.sister1 = "Gopi"
        self.sister2 = "Poonam"
        self.brother = "Jaymin"

    def show(self):
        super().show_grand_info()
        super().show_parent_info()
        print(f"Sister name is : {self.sister1}")
        print(f"Sister name is : {self.sister2}")
        print(f"Brother name is : {self.brother}")


c = Children()
c.show()
