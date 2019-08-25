'''
for i in range(5):
    for j in range(5):
        print(i,j)
'''

'''
*
**
***
****
*****
'''

for i in range(6):
    for j in range(i):
        print('*',end='')
    print()

'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
print("-------------")
'''
12345
1234
123
12
1
'''
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
print("-------------")
'''
1
23
456
78910
'''
k = 0
for i in range(1,5):
    for j in range(i):
        k = k + 1
        print(k,end='')
    print()
print("-------------")

'''
    1
   2 3
 4  5  6
7  8  9  10
'''
x = 0
for i in range(1,5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        x += 1
        print(x,end=' ')
    print()




