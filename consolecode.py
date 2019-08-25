Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = "hello how are you ?"
>>> msg.encode()
b'hello how are you ?'
>>> msg = "नमस्ते आप कैसे हैं ?"
>>> msg.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
>>> x = "\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 "
>>> x = b"\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82"
>>> x.decode()
'कैसे हैं'
>>> x = msg.encode()
>>> x
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
>>> x.decode()
'नमस्ते आप कैसे हैं ?'
>>> msg = x.decode()
>>> msg
'नमस्ते आप कैसे हैं ?'
>>> import sys
>>> sys.getsizeof(msg)
114
>>> a = 0
>>> sys.getsizeof(a)
24
>>> a = 1
>>> sys.getsizeof(a)
28
>>> a = 100
>>> sys.getsizeof(a)
28
>>> a = 100000000
>>> sys.getsizeof(a)
28
>>> a = 10000000000
>>> sys.getsizeof(a)
32
>>> a = 10000000000000000000
>>> sys.getsizeof(a)
36
>>> a = 1000000000000000000000
>>> sys.getsizeof(a)
36
>>> sys.getsizeof(int)
400
>>> sys.getsizeof(int())
24
>>> 2 ** 23
8388608
>>> s ** 27
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s ** 27
NameError: name 's' is not defined
>>> 2 ** 27
134217728
>>> a = 100
>>> id(a)
140723928592112
>>> id(100)
140723928592112
>>> type(a)
<class 'int'>
>>> isinstance(a,int)
True
>>> x = [3,5,6,8,9,4,5]
>>> 
