# Nested Functions

def calc():
    x = 12
    y = 21
    def add():
        return x + y
    def sub():
        return x - y

    return add,sub

x = calc()
print(x[0]())