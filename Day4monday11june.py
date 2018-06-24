Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = [1,2,3,4,5]
>>> l.append(6)
>>> l
[1, 2, 3, 4, 5, 6]
>>> l.append([7,8,9])
>>> l
[1, 2, 3, 4, 5, 6, [7, 8, 9]]
>>> l.extend([7,8,9])
>>> l
[1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9]
>>> l + [10,11,12]
[1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 10, 11, 12]
>>> l.insert(0,0)
>>> l
[0, 1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9]
>>> l.pop()
9
>>> l
[0, 1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8]
>>> l.pop(5)
5
>>> l
[0, 1, 2, 3, 4, 6, [7, 8, 9], 7, 8]
>>> l.pop([7,8,9])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.pop([7,8,9])
TypeError: 'list' object cannot be interpreted as an integer
>>> l.clear()
>>> l
[]
>>> l.pop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.pop()
IndexError: pop from empty list
>>> >>> l = [1,2,3,4,5]
>>> l.append(6)
>>> l
SyntaxError: invalid syntax
>>> l = [1,2,3,4,5]
>>> l.append(6)
>>> l
SyntaxError: multiple statements found while compiling a single statement
>>> l.extend([1,2,3,4,5])
>>> l
[1, 2, 3, 4, 5]
>>> l.pop(0)
1
>>> l
[2, 3, 4, 5]
>>> l.count(2)
1
>>> l.extend([6,7,8])
>>> l
[2, 3, 4, 5, 6, 7, 8]
>>> l.extend([3,2])
>>> l
[2, 3, 4, 5, 6, 7, 8, 3, 2]
>>> l.sort
<built-in method sort of list object at 0x0000008D4B403608>
>>> l.sort()
>>> l
[2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> l.sort(reverse=True)
>>> l
[8, 7, 6, 5, 4, 3, 3, 2, 2]
>>> l[-1::-1]
[2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> l.reverse()
>>> l
[2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> a=[1,2,3]
>>> b=a
>>> b==a
True
>>> b is a
True
>>> b[1]=3
>>> b
[1, 3, 3]
>>> a
[1, 3, 3]
>>> l
[2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> l.append([2,3,4])
>>> l
[2, 2, 3, 3, 4, 5, 6, 7, 8, [2, 3, 4]]
>>> l.pop(9)
[2, 3, 4]
>>> l
[2, 2, 3, 3, 4, 5, 6, 7, 8]
>>> c=b.copy()
>>> c
[1, 3, 3]
>>> b
[1, 3, 3]
>>> a
[1, 3, 3]
>>> c[1]=2
>>> a
[1, 3, 3]
>>> b
[1, 3, 3]
>>> c
[1, 2, 3]
>>> d is c
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d is c
NameError: name 'd' is not defined
>>> d = c.copy()
>>> d is c
False
>>> d==c
True
>>> l = []
>>> for i in range (10):
	i.append(i**2)
	print(l)
	
KeyboardInterrupt
>>>  print([i**2 for i in range (10)])
SyntaxError: unexpected indent
>>> print([i**2 for i in range (10)])
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a==10
False
>>> u==10
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    u==10
NameError: name 'u' is not defined
>>> a==10
False
>>> p==10
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    p==10
NameError: name 'p' is not defined
>>> a=10
>>> if a>10:
	print("IF BLOCK")
elif a == 10:
	print("ELIF BLOCK")
else:
	print("PYTHON PROGRAMMING")

	
ELIF BLOCK
>>>  l = []
>>> for i in range (10):
      i.append(i**2)
	print(l)
	
SyntaxError: unexpected indent
>>> 
>>> l = []
>>> for i in range (10):
      i.append(i**2)
print(l)

SyntaxError: invalid syntax
>>> 
=== RESTART: C:/Users/Ujjwal Rajput/Downloads/Python programs/forloop12.py ===
Traceback (most recent call last):
  File "C:/Users/Ujjwal Rajput/Downloads/Python programs/forloop12.py", line 3, in <module>
    i.append(i**2)
AttributeError: 'int' object has no attribute 'append'
>>> 
=== RESTART: C:/Users/Ujjwal Rajput/Downloads/Python programs/forloop12.py ===
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> l = []
>>> for i in range(int(input("How many students data do you want to enter:\)))
			     
SyntaxError: EOL while scanning string literal
>>> l = []
>>> for i in range(int(input("How many students data do you want to enter:\))):
			     
SyntaxError: multiple statements found while compiling a single statement
>>> l = []
>>> for i in range(int(input("How many students data do you want to enter:\"))):
			     
SyntaxError: multiple statements found while compiling a single statement
>>> a= input("Enter name:\n")
			     
Enter name:
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a= input("Enter name:\n")
KeyboardInterrupt
>>> l = []
>>> for i in range(int(input("How many students data do you want to enter:\n")))
			     
SyntaxError: multiple statements found while compiling a single statement
>>> l = []
>>> for i in range(int(input("How many students data do you want to enter:\n"))):
			     
SyntaxError: multiple statements found while compiling a single statement
>>> char(97)
			     
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    char(97)
NameError: name 'char' is not defined
>>> chr(97)
			     
'a'
>>> ord('a')
			     
97
>>> l= []
for i in range(int(input("How many students data do you want to enter:\n")))
a =input(“Enter name:\n”)
b =int(input(“Enter marks:\n”))
grade = ‘ ‘
if b >=81 and b<=100:
grade = “A+”
elif b>=70 and b<=80:
grade =”A”
else:
grade = “B”
l.append([a,grade])
(l)

SyntaxError: multiple statements found while compiling a single statement
>>> a = 'abcdefghijklmnopqrstuvwxyz'
			     
>>> l=list(a)
			     
>>> for i in l:
			     print(ord(i))

			     
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
>>>  import string
 for i in list(string.ascii_lowercase):
 print(ord(i))
			     
SyntaxError: unexpected indent
>>> import string
 for i in list(string.ascii_lowercase):
 print(ord(i))
			     
SyntaxError: multiple statements found while compiling a single statement
>>> import string
			     
 for i in list(string.ascii_lowercase):
      print(ord(i))
			     
SyntaxError: multiple statements found while compiling a single statement
>>> import string
			     
>>> for i in list(string.ascii_lowercase):
			     print(ord(i))

			     
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
>>> print([i,j]) for i in [1,2,3,4,5] for j in ['a','b','c']]
		       
SyntaxError: invalid syntax
>>> print([i,j] for i in [1,2,3,4,5] for j in ['a','b','c']])
		   
SyntaxError: invalid syntax
>>> print([i,j] for i in [1,2,3,4,5] for j in ['a','b','c'])
		   
<generator object <genexpr> at 0x00000020538A5A40>
>>> print( ([i,j]) for i in [1,2,3,4,5] for j in ['a','b','c'])
		   
<generator object <genexpr> at 0x00000020538A5A40>
>>> 
		   
>>> [print([i,j]) for i in [1,2,3,4,5] for j in ['a','b','c']]
		   
[1, 'a']
[1, 'b']
[1, 'c']
[2, 'a']
[2, 'b']
[2, 'c']
[3, 'a']
[3, 'b']
[3, 'c']
[4, 'a']
[4, 'b']
[4, 'c']
[5, 'a']
[5, 'b']
[5, 'c']
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> dict_comp = {char(65+x) for x in range(1,11)}
		   
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    dict_comp = {char(65+x) for x in range(1,11)}
  File "<pyshell#111>", line 1, in <setcomp>
    dict_comp = {char(65+x) for x in range(1,11)}
NameError: name 'char' is not defined
>>> dict_comp = {chr(65+x) for x in range(1,11)}
		   
>>> print(dict_comp)
		   
{'J', 'I', 'C', 'E', 'D', 'K', 'G', 'B', 'H', 'F'}
>>> set_comp = {x** for x in range(10) if x%2==0}
		   
SyntaxError: invalid syntax
>>> a={x**3 for x in range(10) if x%2==0}
		   
>>> print(a)
		   
{0, 64, 512, 8, 216}
>>> hasattr(str,'__iter')
		   
False
>>>  hasattr(int, '__iter__')
		   
SyntaxError: unexpected indent
>>> hasattr(str,' __iter__')
		   
False
>>> hasattr(int, '__iter__')
		   
False
>>>  hasattr(list, '__iter__')
		   
SyntaxError: unexpected indent
>>> hasattr(list, '__iter__')
		   
True
>>> from sys import getsizeof
		   
>>> my_comp = [x*5 for xin range(1000)]
		   
SyntaxError: invalid syntax
>>> from sys import getsizeof
		   
>>> my_comp = [x*5 for x in range(1000)]
		   
>>> my_gen = (x*5 for x in range(1000)]
		   
SyntaxError: invalid syntax
>>> my_gen = (x*5 for x in range(1000))
		   
>>> print(getsizeof(my_comp))
		   
9024
>>> print(getsizeof(my_gen))
		   
88
>>> from sys import getsizeof
		   
>>> my_comp = [x*5 for x in range(1000)]
		   
>>> my_gen = (x*5 for x in range(1000))
		   
>>> print(getsizeof(my_comp))
		   
9024
>>> print(getsizeof(my_gen))
		   
88
>>> for i in range(1,20):
		   if i==10:
		   break
		   
SyntaxError: expected an indented block
>>> for i in range(1,20):
		    if i==10:
		          break
		   else:
		   
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(1,20):
		    if i==10:
		          break
		      else:
		   
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(1,20):
		    if i==10:
		          break
		    else:
		        print(i)
   for i in range(1,10):
		   
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(1,20):
		    if i==10:
		          break
		    else:
		        print(i)
for i in range(1,10):
		   
SyntaxError: invalid syntax
>>> for i in range(1,20):
		    if i==10:
		          break
		    else:
		        print(i)
    for i in range(1,10):
		   
SyntaxError: unindent does not match any outer indentation level
>>> if i ==5:
		   continue
		   
SyntaxError: 'continue' not properly in loop
>>> else:
		   
SyntaxError: invalid syntax
>>> print(i)
		   
z
>>> for i in range(1,10):
		   if i ++5:
		   pass
		   
SyntaxError: expected an indented block
>>> 
