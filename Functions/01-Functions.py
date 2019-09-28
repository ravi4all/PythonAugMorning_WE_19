# global scope
x = 21
y = 33

def add():
    # local scope
    x = 12
    y = 21
    z = x + y
    print("Sum is",z)

add()
z = x - y