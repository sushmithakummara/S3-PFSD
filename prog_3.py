#functions
"""class Student:
    id=10
    name="sushmitha"
    def display(self):
        print(self.id)
s1=Student()
print(s1.display())"""

#cunstructors
"""class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
s1=Student(19,"kummara")
s2=Student(20,"sushmitha")
print(s1.display())
print(s2.display())"""

#class-objects
"""class Sushmitha:
    x="learing starts with"
    y="joy"
    def display(self):
        print("the result starts from",self.x,self.y)
s=Sushmitha()
print(s.display())"""


#constructors with non-parametrised
"""class Student:
    count=0
    def __init__(self):
        Student.count+=1
s1=Student()
s2=Student()
print(s1.count)"""

#morethan one constructor
"""class Dog:
    def __init__(self,id):

       print("second")
    def __init__(self):
        print("not parametrised")
d=Dog()
"""