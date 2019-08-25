# Fib Series - 0 1 1 2 3 5 8 13 21 34....

a = 1
b = 0
while b < 200:
    print(b,end=',')
    a,b = b,a+b
