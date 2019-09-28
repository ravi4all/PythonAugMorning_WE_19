def temp_conv(cel):
    return 9/5 * cel + 32

# f = temp_conv(34.5)
# print(f)

temp = [34.4,43.2,36.7,38.7,31.3]

# f = []
# for t in temp:
#     f.append(temp_conv(t))
#
# print(f)

# f = list(map(temp_conv,temp))
# print(f)

def myMap(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = myMap(temp_conv,temp)
print(f)