def even(num): return num % 2 == 0

# e = even(4)
# print(e)

numbers = [i for i in range(1,21)]

# e = []
# for i in range(len(numbers)):
#     if even(numbers[i]):
#         e.append(numbers[i])
#
# print(e)

e = list(filter(even,numbers))
print(e)