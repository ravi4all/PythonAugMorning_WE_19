Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello, this is python"
>>> text[0]
'h'
>>> text[1]
'e'
>>> len(text)
21
>>> text[25]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    text[25]
IndexError: string index out of range
>>> text[0:4]
'hell'
>>> text[0:15]
'hello, this is '
>>> text[0:15:2]
'hlo hsi '
>>> text[15:1]
''
>>> text[15:1:-1]
'p si siht ,oll'
>>> text[15:0:-1]
'p si siht ,olle'
>>> text[15::-1]
'p si siht ,olleh'
>>> text[10:]
's is python'
>>> text[-1]
'n'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'nohtyp si'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.capitalize()
'Hello, this is python'
>>> text.upper()
'HELLO, THIS IS PYTHON'
>>> text.lower()
'hello, this is python'
>>> text.title()
'Hello, This Is Python'
>>> text.count('o')
2
>>> text.count('z')
0
>>> text.find('o')
4
>>> text.find('o',5)
19
>>> text.find('z')
-1
>>> text.rfind('o')
19
>>> text.isdigit()
False
>>> text.isalpha()
False
>>> text.isalnum()
False
>>> text.isprintable()
True
>>> text.center(10)
'hello, this is python'
>>> text.center(20)
'hello, this is python'
>>> text.center(30)
'    hello, this is python     '
>>> len(text)
21
>>> text.center(21)
'hello, this is python'
>>> text.center(22)
'hello, this is python '
>>> text.center(23)
' hello, this is python '
>>> text.center(24)
' hello, this is python  '
>>> text.center(25)
'  hello, this is python  '
>>> text.center(50)
'              hello, this is python               '
>>> text.center(50,')')
'))))))))))))))hello, this is python)))))))))))))))'
>>> text.center(50,'0')
'00000000000000hello, this is python000000000000000'
>>> text.center(50,'*')
'**************hello, this is python***************'
>>> text.encode()
b'hello, this is python'
>>> text.startswith('x')
False
>>> text.endswith('x')
False
>>> text.split()
['hello,', 'this', 'is', 'python']
>>> text.split(',')
['hello', ' this is python']
>>> text.split('o')
['hell', ', this is pyth', 'n']
>>> '-'.join(text.split())
'hello,-this-is-python'
>>> text
'hello, this is python'
>>> text.replace('o','i')
'helli, this is pythin'
>>> text
'hello, this is python'
>>> text = '**************hello, this is python***************'
>>> text.strip()
'**************hello, this is python***************'
>>> text.strip('*')
'hello, this is python'
>>> text = '              hello, this is python               '
>>> text.strip()
'hello, this is python'
>>> a = [2,3,4,6,8]
>>> b = [4,6,6,3,3]
>>> a = [2,3,4,6,8]
>>> 2 in a
True
>>> text.partition()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    text.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> text.partition(' ')
('', ' ', '             hello, this is python               ')
>>> text
'              hello, this is python               '
>>> text = text.strip()
>>> text.partition(',')
('hello', ',', ' this is python')
>>> text.split(',')
['hello', ' this is python']
>>> text.partition('o')
('hell', 'o', ', this is python')
>>> text.split()
['hello,', 'this', 'is', 'python']
>>> text.rsplit('o')
['hell', ', this is pyth', 'n']
>>> text.split('o')
['hell', ', this is pyth', 'n']
>>> 
