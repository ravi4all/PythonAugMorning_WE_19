Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {"action":5,"comedy":6,"thriller":8,"horror":3}
>>> max(d)
'thriller'
>>> d = {"action":5,"comedy":6,"thriller":8,"horror":3,"drama":12}
>>> max(d)
'thriller'
>>> max(d.items())
('thriller', 8)
>>> max(d.values())
12
>>> d.keys()
dict_keys(['action', 'comedy', 'thriller', 'horror', 'drama'])
>>> list(d.values()).index(max(d.values()))
4
>>> d.keys()[4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.keys()[4]
TypeError: 'dict_keys' object is not subscriptable
>>> list(d.keys())[4]
'drama'
>>> list(d.keys())list(d.values()).index(max(d.values()))
SyntaxError: invalid syntax
>>> list(d.keys())[list(d.values()).index(max(d.values()))]
'drama'
>>> d
{'action': 5, 'comedy': 6, 'thriller': 8, 'horror': 3, 'drama': 12}
>>> d.values()
dict_values([5, 6, 8, 3, 12])
>>> max(d.values())
12
>>> list(d.values())
[5, 6, 8, 3, 12]
>>> list(d.values()).index(max(d.values()))
4
>>> d.keys()
dict_keys(['action', 'comedy', 'thriller', 'horror', 'drama'])
>>> d.keys()[4]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d.keys()[4]
TypeError: 'dict_keys' object is not subscriptable
>>> list(d.keys())[list(d.values()).index(max(d.values()))]
'drama'
>>> max(d)
'thriller'
>>> max(d.items())
('thriller', 8)
>>> max(d.items(),key=lambda x : x[1])
('drama', 12)
>>> def show(x):
	return x[1]

>>> max(d.items(),key=show(d.items()))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    max(d.items(),key=show(d.items()))
  File "<pyshell#25>", line 2, in show
    return x[1]
TypeError: 'dict_items' object is not subscriptable
>>> max(d.items(),key=show)
('drama', 12)
>>> 
