#OOPS
#Syntax
'''class classname():
    #attributes
    name="codegnan"
    year=2026
    place="vja"
    def fname(self):
        print(statements....._)
a=classname()
a.fname()''' #Error

#class decleration
'''
class Details():
    name="Yaseer"
    age="22"
    place="vja"
    def fname(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.fname()
'''

#Object instantiation
'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("Yaseer",21,"Vja")
a.display()
b=Details()
b.Data("Raj",23,"Vja")
b.display()
c=Details()
c.Data("Harsha",20,"Vja")
c.display()'''

'''
class Details():
    def Data(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data()
a.display()'''


#Object initialization
'''
class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("Shaik",25,"VIJ")
print(dir(a))
a.display()'''


#Diff between _ & __ :
'''we generally use it for private variables ,
that means whenever we use double leading _(underscore) our python interpreter
reads it as a special variable in order to avoids name conflicts with methods
and inner classes '''

'''
class Employee():
    def __init__(self):
        self.name="Yaseer"
        self.__salary=10000#private variable
        self._mailid="Yaseer@gmail.com"
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee__salary)

class Employee1():
    def __init__(self):
        self.name="Likit"
        self.__salary=20000#private variable
        self._mailid="Likit@gmail.com"

b=Employee1()
#print(dir(b))
print(b.name)
print(b._mailid)
print(b._Employee1__salary)

class Employee2():
    def __init__(self):
        self.name="Ram"
        self.__salary=30000#private variable
        self._mailid="Ram@gmail.com"

c=Employee2()
#print(dir(c))
print(c.name)
print(c._mailid)
print(c._Employee2__salary)
'''

#Polymorphism:
#Operator overloading

'''
a=3;b=5
print(a+b)
print(a.__add__(b))
print(a.__add__(6))
print(a.__sub__(2))
print(a.__mul__(4))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__ge__(2))
print(a.__le__(4))
a=[1,2,3,4,5];b=[5,6,7,8,9]
print(a.__add__(b))
print(a.__getitem__(2))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))
print("yaseer".__add__(" "+"shaik").title())
'''


#Operator overriding:

'''
class A():
    def __init__(self,a):
        self.a=a
    def __add__(self, value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)
y=B(5)
#x=4
#y=5
print(x+y)
'''

#Method overloading:

'''
class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is:",a*b)
        else:
            print("program ends...")
a=New()
a.sum(2,3,4)
a.sum()
a.sum(5,6)'''


#Method overriding:

'''
class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("Dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()

'''

class Bike1():
    def ride(self):
        print("Rider 1 overtakes rider2")
class Bike2():
    def ride(self):
        print("Rider 2 stays still")
a=Bike1()
b=Bike2()
a.ride()
b.ride()












































