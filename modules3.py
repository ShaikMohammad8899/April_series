#regex(Regular Expression):
'''regular expressions are powerful tools(module)embedded in python . which is mainly is used to find a pattern with in a given string
or statements or files and we mainly use it for text manipulation'''

'''
a="codegnan\nis\nin\tvijayawada"
print(a)
'''

#rstring(Raw string)
'''
a=r"codegnan\nis\nin\tvijayawada"
print(a)
'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''
\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\S->it represents non-white spaces
'''

import re
a="mat cat map maths cash money monkey donkey cap dog log"

'''
b=re.compile(r"m\w\w\w\w")
print(b)
c=b.search(a)
print(c)'''

'''
d=re.search(r"m\w+",a)
print(d)
'''

#findall()
'''
e=re.findall(r"m\w+",a)
print(e)
print(*e)
'''

'''
x=re.split(r"m\w+",a)
print(x)
'''

'''
y=re.split(r"m\w",a)
print(y)
'''

'''
z=re.split(r"m",a)
print(z)
'''
'''
z=re.split(r"\s",a)
print(z)
'''
'''
z=re.split(r"\S",a)
print(z)
'''
'''
z=re.sub(r"m","a",a)
print(z)
'''
'''
z=re.sub(r"monkey","likith",a)
print(z)'''

'''
import re
a="year 2026 month 4 date 4"
b=re.findall(r"\d+",a)
print(b)
'''

'''
d="year 2026 month 444444 date 4"
c=re.search(r"\d+",a)
print(c)
'''



