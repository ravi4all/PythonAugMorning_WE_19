Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turt = turtle.Pen()
>>> turt.shape('turtle')
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.forward(200)
>>> turt.left(90)
>>> turt.reset()
>>> for i in range(4):
	turt.forward(200)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(25):
	turt.forward(4*i)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> for i in range(4,40):
	turt.forward(4*i)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(25):
	turt.circle(4*i)
	turt.left(90)

	
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(250):
	turt.circle(4*i)
	turt.left(90)

	
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_1.py 
0
1
2
3
4
5
6
7
8
9
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_1.py 
0
1
2
3
4
5
6
7
8
9
---------------
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_1.py 
0
1
2
3
4
5
6
7
8
9
---------------
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
---------------
10
15
20
25
30
35
40
45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_1.py 
0
1
2
3
4
5
6
7
8
9
---------------
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
---------------
5
10
15
20
25
30
35
40
45
50
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_2.py 
Enter the number10
10
20
30
40
50
60
70
80
90
100
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_2.py 
Enter the number6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
>>> 'hello'*5
'hellohellohellohellohello'
>>> 'hello' + 5
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    'hello' + 5
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_3.py 

*
**
***
****
*****
******
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_3.py 

*
**
***
****
*****
******
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
>>> for i in range(5):
	print('*')

	
*
*
*
*
*
>>> for i in range(5):
	print('*',end='')

	
*****
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 
***************
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****

1
22
333
4444
55555
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****

0
01
012
0123
01234
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
>>> for i in range(10,1,-1):
	print(i)

	
10
9
8
7
6
5
4
3
2
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
123456
12345
1234
123
12
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
-------------
123456
12345
1234
123
12
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
-------------
123456
12345
1234
123
12
1
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
-------------
123456
12345
1234
123
12
1
-------------
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py", line 50, in <module>
    k - 0
NameError: name 'k' is not defined
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonWE/loops_4.py 

*
**
***
****
*****
1
12
123
1234
12345
-------------
123456
12345
1234
123
12
1
-------------
1
23
456
78910
>>> 
