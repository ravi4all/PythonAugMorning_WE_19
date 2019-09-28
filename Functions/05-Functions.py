# *args and **kwargs

def add(*x):
    # print(x)
    s = 0
    for i in x:
        s += i

    print(s)

add(4,5)
add(5,6,7)
add(4,8,2,4,67,9)
add(2,3,5,7,1)

def emp(**details):
    print(details)

emp(name='ram',sal=34000,dept='IT')
emp(name='Shyam',address='Delhi',desig='Developer')