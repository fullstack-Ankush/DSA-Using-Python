# solution 1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"my name is {self.name} and i am {self.age} year old ")


p1 = Person("Ankush",21)

p1.show()