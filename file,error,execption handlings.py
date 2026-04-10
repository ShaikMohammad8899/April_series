##File Handling:

#write()
'''
a.open("yaseer .txt/"w)
a.write("codegnan"")
        a.close()

'''

'''
a=open("yaseer.txt","w")
a.write("python")
a.close()
'''


''' XXXXXX
a=open("yaseer.txt","w")
a.write("python")
a.close()


append()

a=-open("poojann.txt"."s")
a.write'''


'''
a=open("yaseer.txt","w")
b=input("data:")
a.write(b)
a.close()
'''


#read()
'''
a=open("yaseer.txt")
#print(a.read()) #it will display entire content
#print(a.readline()) #it will display first line
#print(a.readlines()) #it will display with \n
print(a.read(15))#it will display no.of characters
'''


#WriteLines()

'''
names=["siva","tejaswi","devi","revanth","arvind"]
a=open("pooja.txt","w")
a.writelines("\n".join(names))
a.close()
'''

'''
a=open("data.py")
print(a.read())
'''

'''
a=open("C:\\Users\\Dell\\OneDrive\\Desktop\\codegnan\\pics\\modules2.py")
print(a.read())
'''


##Error handling:
'''
1.syntax error : complie error
2.Run_Time Error : During excecution time it will happen
3.Logical_error : Error in logic(it can't be visible)
'''

#1.Syntax Error:

'''
a=int(input("enter a value:"))
for i in range(1,a)
print(i)
'''

#2.Run_time Error:

'''
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(a//b)
'''

#3.Logical Error:
'''
a=10
b=20
print(a-b)
'''

'''
a=3
b=6
if a<b:
    print("true")
'''

##Exception Handling:

'''1.Try,2.Except,3.Finally,4.Else'''
#Try: instructions from which are expecting the exceptions
#except: error is raised in try block it will handle by this block
#else: optional(no exceptions)
#finally: always it will print


while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    try:
        c=a//b
        print(c)
    except:
        print("Exception is raised")
    else:
        print("no Exception")
    finally:
        print("program ends")


















