class Student:
    def __init__(self, rollNo, name):
        self.rollNo=rollNo
        self.name=name
    def printName(self):
        print("Name in Object : ",self.name)

s1=Student(103,"jay")
s1.printName()
