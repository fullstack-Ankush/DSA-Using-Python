# solution 1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"my name is {self.name} and i am {self.age} year old ")


p1 = Person("Ankush",21)

p1.show()

# solution 2

class Circle:
    def __init__(self,r):
        self.radius = r

    def setter(self,value):
        self.radius = value

    def getter(self):
        print(self.radius)
c1 = Circle(5)
c1.setter(15)
c1.getter()


# solution 3

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breath = b

    def setDimenstion(self,l=1,b=1):
        self.length = l
        self.breath = b

    def showDimension(self):
        print(f"Length = {self.length} Breath = {self.breath}")

    def getArea(self):
        return self.breath * self.length


r1 = Rectangle(10,4)
print(r1.getArea())

