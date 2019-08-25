a = 34
b = 44
c = a + b
d = a - b
e = a / b
f = a * b
print(c)
print("Sum is",c)
print("Sum is %d"%c)
print("Sum of", a, "and", b, "is", c)
print("Sum of %d and %d is %d"%(a,b,c))
print("Sum of {} and {} is {}".format(a,b,c))
print(f"Sum of {a} and {b} is {c}")

print(f"""
Add is {c}
Sub is {d}
Div is {e}
Mul is {f}
""")
