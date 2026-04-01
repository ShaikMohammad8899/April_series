#difference between module,library and package :
#module:
'''
1.A module in python is a single python file consists python code
2.It typically concists of functions,classes and variables that can be used in other python scripts or programs
3.examples of modules such as "math.py,random.py,mymodule.py"
'''

#package:
'''
1.a package in python is alibrary containing one or more python modules and an init.py file
2. the init.py file can be empty or contain initialization code for the package
3.examples of package include numpy,pandas,django'''


#library:
'''
1.libraries can consists of multiple modules and packages ,organized to serve a particular purpose or domian
2.example of libraries such as requests,numpy,pandas and matplotlib'''


#note:
'''
every python file is a module and import is a keyword and every python file is saved internally with variable name as "__main__" '''


'''
def greet(name):
    print("welcome",name)
'''

'''
a=4
b=10
print(a+b)
'''

'''
a=int(input("A value"))
b=int(input("b value"))
print(a+b)
'''

'''
Details={"idnos":[10,20,30,40],
         "names":["ram","likit","mani","jack"],
         "places":["vij","hyd","viz","chennai"]}
'''

'''
if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
   print(a)
'''

def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()

















