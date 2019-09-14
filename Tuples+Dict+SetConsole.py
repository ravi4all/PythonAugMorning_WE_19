Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 2,4,5,6
>>> x = (2,4,5,6)
>>> x = 2,
>>> type(x)
<class 'tuple'>
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> import sys
>>> sys.getsizeof(tuple())
48
>>> sys.getsizeof(list())
64
>>> x1 = (i for i in range(10))
>>> x1 = [i for i in range(10)]
>>> x2 = (i for i in range(10))
>>> sys.getsizeof(x1)
192
>>> sys.getsizeof(x2)
120
>>> x1 = [i for i in range(10000)]
>>> x2 = (i for i in range(10000))
>>> sys.getsizeof(x1)
87624
>>> x2 = (i for i in range(10000))
>>> sys.getsizeof(x2)
120
>>> x2
<generator object <genexpr> at 0x000001F7E22C78B8>
>>> type(x2)
<class 'generator'>
>>> emp = name,age,sal = 'ram',30,25000
>>> emp
('ram', 30, 25000)
>>> name
'ram'
>>> age
30
s
>>> sal
25000
>>> emp = name,age,sal = ['ram',30,25000]
>>> emp
['ram', 30, 25000]
>>> name = 'shyam'
>>> emp
['ram', 30, 25000]
>>> name
'shyam'
>>> data = {"name":"Ram","sal":45000,"dept":"IT","company":"IBM"}
>>> data
{'name': 'Ram', 'sal': 45000, 'dept': 'IT', 'company': 'IBM'}
>>> type(data)
<class 'dict'>
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["dept"]
'IT'
>>> data["name"]
'Ram'
>>> data["sal"] = 48000
>>> data["address"] = "Delhi"
>>> data
{'name': 'Ram', 'sal': 48000, 'dept': 'IT', 'company': 'IBM', 'address': 'Delhi'}
>>> data.keys()
dict_keys(['name', 'sal', 'dept', 'company', 'address'])
>>> data.values()
dict_values(['Ram', 48000, 'IT', 'IBM', 'Delhi'])
>>> data.items()
dict_items([('name', 'Ram'), ('sal', 48000), ('dept', 'IT'), ('company', 'IBM'), ('address', 'Delhi')])
>>> for item in data:
	print(item)

	
name
sal
dept
company
address
>>> for item in data.values():
	print(item)

	
Ram
48000
IT
IBM
Delhi
>>> for item in data.items():
	print(item)

	
('name', 'Ram')
('sal', 48000)
('dept', 'IT')
('company', 'IBM')
('address', 'Delhi')
>>> user = {}
>>> user["name"] = input("Enter name : ")
Enter name : Ram
>>> usetr
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    usetr
NameError: name 'usetr' is not defined
>>> user
{'name': 'Ram'}
>>> user["college"] = input("Enter college : ")
Enter college : IP
>>> user
{'name': 'Ram', 'college': 'IP'}
>>> data = {"articles":[{"title":"Apple Introduces new Iphone","desc":"...."},{"title":"Apple Introduces new Iphone","desc":"...."},{"title":"Apple Introduces new Iphone","desc":"...."},{"title":"Apple Introduces new Iphone","desc":"...."},{"title":"Apple Introduces new Iphone","desc":"...."}]}
>>> data
{'articles': [{'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}]}
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['articles'])
>>> data["articles"]
[{'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}, {'title': 'Apple Introduces new Iphone', 'desc': '....'}]
>>> articles = data["articles"]
>>> type(articles)
<class 'list'>
>>> articles[0]
{'title': 'Apple Introduces new Iphone', 'desc': '....'}
>>> articles[0][]
SyntaxError: invalid syntax
>>> 
>>> articles[0]['title']
'Apple Introduces new Iphone'
>>> data = {"names":["ram","shyam","raman","suman","kunal"],"sal":[34000,43000,21000,28000,34000]}
>>> data["names"]
['ram', 'shyam', 'raman', 'suman', 'kunal']
>>> data["sal"]
[34000, 43000, 21000, 28000, 34000]
>>> data["names"][0]
'ram'
>>> data["names"][1]
'shyam'
>>> data = {"names":["ram","shyam","raman","suman","kunal"],"sal":[34000,43000,21000,28000,34000],"dept":["hr","hr","it","it","sales"]}
>>> for i in range(len(data["names"])):
	print(data["names"][i],data["sal"][i],data["dept"][i])

	
ram 34000 hr
shyam 43000 hr
raman 21000 it
suman 28000 it
kunal 34000 sales
>>> for i in range(len(data["names"])):
	for key in dataL
	
SyntaxError: invalid syntax
>>> for i in range(len(data["names"])):
	for key in data:
		print(data[key][i])

		
ram
34000
hr
shyam
43000
hr
raman
21000
it
suman
28000
it
kunal
34000
sales
>>> for i in range(len(data["names"])):
	for key in data:
		print(data[key][i],end='')
	print()

	
ram34000hr
shyam43000hr
raman21000it
suman28000it
kunal34000sales
>>> for i in range(len(data["names"])):
	for key in data:
		print(data[key][i],end=',')
	print()

	
ram,34000,hr,
shyam,43000,hr,
raman,21000,it,
suman,28000,it,
kunal,34000,sales,
>>> data = [{"name":"Ram","age":28,"sal":45000},{"name":"Shyam","age":29,"sal":45000},{"name":"kunal","age":28,"sal":34000}]
>>> for item in data:
	print(item)

	
{'name': 'Ram', 'age': 28, 'sal': 45000}
{'name': 'Shyam', 'age': 29, 'sal': 45000}
{'name': 'kunal', 'age': 28, 'sal': 34000}
>>> item
{'name': 'kunal', 'age': 28, 'sal': 34000}
>>> s1 = {4,5,7,3,4,78,9,3,12,34,6,7,5,8,3}
>>> s1
{34, 3, 4, 5, 6, 7, 8, 9, 12, 78}
>>> s2 = {4,6,8,3,4,6,8,9,0,5,2,12,21,32,6}
>>> s2
{0, 32, 2, 3, 4, 5, 6, 8, 9, 12, 21}
>>> s1 & s2
{3, 4, 5, 6, 8, 9, 12}
>>> s1 | s2
{0, 2, 3, 4, 5, 6, 7, 8, 9, 12, 78, 21, 32, 34}
>>> s1 - s2
{34, 78, 7}
>>> s2 - s1
{0, 32, 2, 21}
>>> s1.intersection(s2)
{3, 4, 5, 6, 8, 9, 12}
>>> s1.union(s1)
{34, 3, 4, 5, 6, 7, 8, 9, 12, 78}
>>> 
