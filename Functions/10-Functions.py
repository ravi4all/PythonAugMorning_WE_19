temp = [34.4,43.2,36.7,38.7,31.3]

f = list(map(lambda c : 9/5 * c + 32,temp))
print(f)


numbers = [i for i in range(1,21)]
e = list(filter(lambda e : e % 2 == 0, numbers))
print(e)