def add(x,y):
    z = x + y
    print("sum is",z)

def sub(x,y):
    z = x - y if x > y else y - x
    print("diff is",z)

def div(x,y):
    z = x / y if y != 0 else x/1
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")
ch = int(input("Enter your choice : "))

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

# operations = [add,sub,div,mul]
# operations[ch - 1](num_1,num_2)

operations = {
    1 : add,
    2 : sub,
    3 : div,
    4 : mul
}

operations.get(ch)(num_1,num_2)