"""class Calculation:
      def perimeter1(self,l,b):
         self.l=l
         self.b=b
         print(2 * (l + b))
      def area1(self,l,b):
          self.l = l
          self.b = b
          print(l*b)
      def perimeter2(self,r):
          self.r=r
          print(2*3.14*r)
      def area2(self,r):
          self.r=r
          print(3.14*r*r)
      def perimeter3(self,br,h):
          self.br=br
          self.h=h
          print((1/2)*br*h)
ob=Calculation()
ob.perimeter1(2,3)
ob.area1(4,5)
ob.perimeter2(4)
ob.area2(6)
ob.perimeter3(5,6)"""
class Trainbook:
     name=input("eneter your name")
     id=input("enter your id number")
     print("your name" + name)
     print("your id "+str(id))
     print("available domains A/C ,GENERAL")
class Registration(Trainbook):
    no_of_seats=60
    if no_of_seats==0 :
        print("no seat is available")
    else:
        seats=0
        seats-=no_of_seats
        print("the available seat number"+str(seats))



