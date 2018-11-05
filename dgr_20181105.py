Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
	
>>> 
>>> 
	
>>> 
>>> 
	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 	
>>> 	
>>> 	
>>> 	
>>> 	
	
>>> 
>>> 
>>> 
>>> 
>>> 	
>>> 
	
>>> 
>>> 
>>> 
>>> 
	
>>> 
>>> 	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> greet= 'Hello Bob '
>>> zap= greet.lower()
>>> print(zap)
hello bob 
>>> print(greet)
Hello Bob 
>>> print('Hi There'.lower())
hi there
>>> stuff='Hello world'
>>> type(stuff)
<type 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fruit='banana'
>>> pos= fruit.find('na')
>>> print(pos)
2
>>> aa=fruit.find('z')
>>> print(aa)
-1
>>> greet= " Hello Bob'
SyntaxError: EOL while scanning string literal
>>> greet= 'Hello Bob'
>>> nnn=greet.upper()
>>> print(nnn)
HELLO BOB
>>> www=greet.lower()
>>> print(www)
hello bob
>>> greet= 'Hello Bob'
>>> nstr= greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr= greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> greet= '  Hello Bob  '
>>> greet.lstrip()
'Hello Bob  '
>>> greet.rstrip()
'  Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line= 'Please have a nice day'
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
>>> data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> atpos=data.find('@')
>>> print(atpos)
21
>>> sppos=data.find('',atpos)
>>> print(sppos)
21
>>> sppos=data.find('',atpos)
>>> print(sppos)
21
]
>>> sppos=data.find(' ',atpos)
>>> print(sppos)
31
>>> host=data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>> [1]
[1]
>>> str1= 'Hello'
>>> str2= 'there'
>>> bob=str1+str2
>>> print(bob)
Hellothere
>>> str3='123
SyntaxError: EOL while scanning string literal
>>> str3='123'
>>> str3= str3 +1

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    str3= str3 +1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x= int(str3)+1
>>> print(x)
124
>>> {2}
set([2])
>>> [2]
[2]
>>> name=input('Enter.')
Enter.Chuck

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    name=input('Enter.')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> name=input('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    name=input('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> apple=input('Enter:')
Enter:100
>>> x=apple-10
>>> x=int(apple)-10
>>> print(x)
90
>>> [3]
[3]
>>> fruit='banana'
>>> letter=fruit[1]
>>> print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> [4]
[4]
>>> zot='abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> [5]
[5]
>>> fruit='banana'
>>> print(len(fruit))
6
>>> [6]
[6]
>>> fruit='banana
SyntaxError: EOL while scanning string literal
>>> fruit='banana'
>>> x-len(fruit)
-3
>>> print(x)
3
>>> x=len(fruit)
>>> print(x)
6
>>> fruit='banana'
>>> x=len(fruit)
>>> print(x)
6
>>> [7]
[7]
>>> fruit='banana
SyntaxError: EOL while scanning string literal
>>> fruit= 'banana'
>>> index= 0
>>> while index < len(fruit):
	letter=fruit[index]
	print(index, letter)
	index=index +1

	
(0, 'b')
(1, 'a')
(2, 'n')
(3, 'a')
(4, 'n')
(5, 'a')
>>> fruit='banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> fruit= 'banana'
>>> for letter in fruit:
	print(letter)

	
b
a
n
a
n
a
>>> index=0
>>> while index < len(fruit):
	letter=fruit[index]
	print(letter)
	index=index+1

	
b
a
n
a
n
a
>>> [8]
[8]
>>> wword='banana'
>>> count= 0
>>> for letter in wod:
	if letter == 'a':
		count= count+1
print(count)
SyntaxError: invalid syntax
>>> 
>>> for letter in wod:
	if letter == 'a':
		count= count+1

		

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    for letter in wod:
NameError: name 'wod' is not defined
>>> for letter in wod:
	if letter == 'a':
		count= count+1
		print(count)

		

Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    for letter in wod:
NameError: name 'wod' is not defined
>>> s= 'Mounty Python'
>>> print(s[0:4])
Moun
>>> print(s[6:7])
 
>>> print(s[6:20])
 Python
>>> s= 'Monty Python'
>>> print(s[:2])
Mo
>>> print(s[8:])
thon
>>> print(s[:])
Monty Python
>>> a='Hello'
>>> b=a+'there'
>>> print(b)
Hellothere
>>> c=a+ ''+'There"
SyntaxError: EOL while scanning string literal
>>> c=a+ ''+'There'
>>> print(c)
HelloThere
>>> fruit='banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan'in fruit
True
>>> if 'a' in fruit:
	print('Found it!')

	
Found it!
>>> if word == 'banana':
	print('All right, bananas.')
if word <'banana':
	
SyntaxError: invalid syntax
>>> if word == 'banana':
	print('All right, bananas.')

	

Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> 
