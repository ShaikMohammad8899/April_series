#annonymous function(nameless functions)
'''annonymous functions are nameless functions and we use a keyword called as
lambda to create annonymous functions'''

#1.write a function to calculate 2*x+5 where x=5
'''
def f(x):
    print(2*x+5)
f(5)
'''

'''
def f():
    x=int(input("enter a value:"))
    print(2*x+5)
f()
'''

#Syntax(a=lambda arg:expr)
'''
a=lambda x:2*x+5
print(a(5))
'''

'''
a=int(input("enter a value:"))
b=lambda x:3*x+5
print(b(a))
'''
#tasks:
'''
a=lambda x,y:y*x
b=lambda x,y:y*x
print(a(5,4))
print(b(5,6))
'''

'''
a=int(input("enter a value:"))
b=int(input("enter a value:"))
c=lambda x,y:3*x+y
d=lambda x,y:5*x*y
print(c(a,b))
print(d(a,b))
'''

'''
a="codegnan"
b=lambda a:a.upper()
print(b(a))
'''

'''
a=lambda a:a.upper()
print(a("codegnan"))
'''

'''
a=input("data:")
b=lambda a:a.upper()
print(b(a))
'''

'''
a="python course"
b=lambda a:a.title()
print(b(a))
'''

'''
a=input("enter first name:")
b=input("enter last name:")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
'''

'''
a,b=[x for x in input("enter the names:").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
'''

'''
a,b=input("enter the names:").split(",")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))
'''

#Filter():

'''
a=[10,20,40,55,67,89,90,97,100]
for i in a:
    if i%2==0:
        print(i,end=" ")
'''

'''
a=[10,20,40,55,67,89,90,97,100]
b=list(filter(lambda a:a%2==0,a))
print(b)
'''

#only none keyword is used to filter none values
'''
a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))
'''

'''
a=[[],(),{},set(),2,2.5,"none",3+5j,True,False]
b=list(filter(None,a))
print(b)
'''


#Map()
'''each object from a collection and forms a new collection'''
'''
a=[10,4,6,8,30,50,100,25]
b=[1,3,5,7,90,56,34,57]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)
'''
'''
a=input("data1:")
b=input("data2:")
print(a+b)
'''

'''
a,b=[x for x in input("enter the names:").split(",")]
print(a+b)
'''

'''
a=int(input("a value"))
b=int(input("b value"))
print(a+b)
'''

'''
a,b=[int(x) for x in input("enter the values:").split(",")]
print(a+b)
'''

'''
a,b=int(input("enter the values:").split(","))
print(a+b)'''#error

'''
a,b=map(int,input("enter the values").split(","))
print(a+b)
'''

'''
a=list(map(int,input("enter the values").split(",")))
print(a)


a=tuple(map(int,input("enter the values").split(",")))
print(a)

a=set(map(int,input("enter the values").split(",")))
print(a)
'''

a = dict(item.split(":") for item in input("enter the values: ").split(","))
print(a)
print(type(a))























