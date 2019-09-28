# def add(x,y):
#     z = x + y
#     # print(z)
#     return z
#
# z = add(4,5)
# print(z)

def calc(x,y):
    return x + y, x - y, x * y, x / y

# z = calc(4,5)
# print(z)

# Packing & Unpacking
# a,b,c,d = calc(4,5)
# print(a,b,c,d)

a,*b = calc(4,5)
print(a,b)