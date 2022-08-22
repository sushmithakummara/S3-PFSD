#inheritence
#single inheritence
"""class Parent:
    def fn1(self):
        print("this is parent class")
class Child(Parent):
    def fn2(self):
        print("this is child class")
c=Child()
print(c.fn1())
print(c.fn2())"""

#multi-level inheritence
"""class Parent:
    def fn1(self):
        print("this is parent class1")
class Child(Parent):
    def fn2(self):
        print("this is parent class2")
class Grand(Child):
    def fn3(self):
        print("this is child one")
ob=Grand()
ob.fn1()
ob.fn2()
ob.fn3()"""


#multiple inheritence
"""class Parent:
    def fn1(self):
        print("one")
class Parent1:
    def fn2(self):
        print("one one")
class Parent2:
    def fn3(self):
        print("one one one")
class Child(Parent,Parent1,Parent2):
    def fn4(self):
        print("yes")
ob=Child()
ob.fn1()
ob.fn2()
ob.fn3()
ob.fn4()"""

#heirarchial
"""class Parent:
    def fn1(self):
        print("one")
class Child(Parent):
    def fn2(self):
        print("two")
class Child1(Parent):
    def fn3(self):
        print("three")
ob=Child()
ob.fn1()
ob.fn2()
ob1=Child1()
ob1.fn1()
ob1.fn3()"""

#hybrid
"""class Parent:
    def fn1(self):
        print("one")
class Child1(Parent):
    def fn2(self):
        print("two")
class Derived(Child1):
    def fn3(self):
        print("three")
ob=Derived()
ob.fn1()
ob.fn2()
ob.fn3()
"""
