Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [2,4,5,2,1,4.56,'hello']
>>> x[0]
2
>>> x[0:4]
[2, 4, 5, 2]
>>> x = []
>>> x.append('hello')
>>> x
['hello']
>>> x.append('bye')
>>> x
['hello', 'bye']
>>> x.append('hi')
>>> x
['hello', 'bye', 'hi']
>>> x = []
>>> for i in range(1,101):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> x = [i for in range(1,101) if i % 2 == 0 ]
SyntaxError: invalid syntax
>>> x = [i for i in range(1,101) if i % 2 == 0 ]
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> x = [i**2 for i in range(10)]
>>> x
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x = [i for i in  range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = list(range(10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.pop()
9
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> x.pop(4)
4
>>> x
[0, 1, 2, 3, 5, 6, 7, 8]
>>> x = [4,5,3.,4,7,9,4,3,3,6,8,23,12,45,75]
>>> x.pop()
75
>>> x.pop(3)
4
>>> x
[4, 5, 3.0, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45]
>>> x.remove(3)
>>> x
[4, 5, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45]
>>> x.remove(11)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.remove(11)
ValueError: list.remove(x): x not in list
>>> del x[1]
>>> x
[4, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45]
>>> y = [21.22,24.55,56.22,43.2]
>>> x.append(y)
>>> x
[4, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45, [21.22, 24.55, 56.22, 43.2]]
>>> x.pop()
[21.22, 24.55, 56.22, 43.2]
>>> x.extend(y)
>>> x
[4, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45, 21.22, 24.55, 56.22, 43.2]
>>> sorted(x)
[3, 3, 4, 4, 6, 7, 8, 9, 12, 21.22, 23, 24.55, 43.2, 45, 56.22]
>>> x
[4, 7, 9, 4, 3, 3, 6, 8, 23, 12, 45, 21.22, 24.55, 56.22, 43.2]
>>> x.sort()
>>> x
[3, 3, 4, 4, 6, 7, 8, 9, 12, 21.22, 23, 24.55, 43.2, 45, 56.22]
>>> x.sort(reverse=True)
>>> x
[56.22, 45, 43.2, 24.55, 23, 21.22, 12, 9, 8, 7, 6, 4, 4, 3, 3]
>>> 
