# Hybrid inheritance
# Hierarchical inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class 1
class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth to live young")

# Derived class 2
class Bird(Animal):
    def lay_eggs(self):
        print(f"{self.name} is laying eggs")

# Derived class 3 using multiple inheritance
class Bat(Mammal, Bird):
    def fly(self):
        print(f"{self.name} is flying")

# Derived class 4 using multilevel inheritance
class Dog(Mammal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Derived class 5 using multilevel inheritance
class Parrot(Bird):
    def speak(self):
        print(f"{self.name} says Squawk!")

# Object of class Bat, demonstrating multiple inheritance
batman = Bat("Batman")
batman.speak()      # This will call the speak method of Mammal class
batman.give_birth() # This will call the give_birth method of Mammal class
batman.lay_eggs()   # This will call the lay_eggs method of Bird class
batman.fly()        # This will call the fly method of Bat class

# Object of class Dog, demonstrating multilevel inheritance
buddy = Dog("Buddy")
buddy.speak()       # This will call the speak method of Dog class
buddy.give_birth()  # This will call the give_birth method of Mammal class

# Object of class Parrot, demonstrating multilevel inheritance
polly = Parrot("Polly")
polly.speak()       # This will call the speak method of Parrot class
polly.lay_eggs()    # This will call the lay_eggs method of Bird class
