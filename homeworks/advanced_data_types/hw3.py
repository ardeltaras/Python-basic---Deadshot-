
##############Start#################

print("# 1. Define the id of next variables:'")
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e), "\n")

print("# 2. Append 4 and 5 to the lst_d and define the id one more time.'")
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d), "\n")

print("# 3. Define the type of each object from step 1.")
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e), "\n")

print("# 4*. Check the type of the objects by using isinstance.")
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict), "\n")

##############String formatting#################

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

print("# 5. With .format and curly braces {}")
print('Anna has {} apples and {} peaches.'.format(3, 2), "\n")

print("# 6. By passing index numbers into the curly braces.")
print('Anna has {1} apples and {0} peaches.'.format(2, 3), "\n")

print("# 7. By using keyword arguments into the curly braces.")
print('Anna has {apples} apples and {peaches} peaches.'.format(apples=3, peaches=2), "\n")

print("# 8*. With indicators of field size (5 chars for the first and 3 for the second)")
print('Anna has {1:5} apples and {0:3} peaches.'.format(2, 3), "\n")

print("# 9. With f-strings and variables")
a = 3
p = 2
print(f'Anna has {a} apples and {p} peaches.', "\n")

print("# 10. With % operator")
print('Anna has %d apples and %d peaches.' % (3, 2), "\n")

print("# 11*. With variable substitutions by name (hint: by using dict)")
apples = 3
peaches = 2
data_dict = {"apples": apples, "peaches": peaches}
print('Anna has %(apples)d apples and %(peaches)d peaches.' % data_dict, "\n")

##############Comprehensions#################

print("# 12. Convert (1) to list comprehension")
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp, "\n")

print("# 13. Convert (2) to regular for with if-else")
# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

list_comp = []
for num in range(10):
    if num % 2 == 0:
        list_comp.append(num // 2)
    else:
        list_comp.append(num * 10)
print(list_comp, "\n")

print("# 14. Convert (3) to dict comprehension.")
# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

d_comp = {num: num ** 2 for num in range(1, 11) if num ** 2 % 2 == 1}
print(d_comp, "\n")

print("# 15*. Convert (4) to dict comprehension.")
# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

d_comp = {num: num ** 2 if num ** 2 % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comp, "\n")

print("# 16. Convert (5) to regular for with if.")
# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

dict_comp = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comp[x] = x ** 3
print(dict_comp, "\n")

print("# 17*. Convert (6) to regular for with if-else.")
# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

dict_comp = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comp[x] = x ** 3
    else:
        dict_comp[x] = x
print(dict_comp, "\n")

##############Lambda#################

print("# 18. Convert (7) to lambda function")
# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(6,5))

foo = lambda x, y: x if x < y else y
print(foo(6,5), "\n")

print("# 19*. Convert (8) to regular function")
# (8)
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(3,6,9))

def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(3,6,9), "\n")

##############End#################

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print("# 20. Sort lst_to_sort from min to max")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort), "\n")

print("# 21. Sort lst_to_sort from max to min")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True), "\n")

print("# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort, "\n")

print("# 23*. Raise each list number to the corresponding number on another list:")
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x: x + 3, list_A))
print(list_C, "\n")

print("# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst_to_sort = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_lst_to_sort, "\n")

print("# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.")
b = range(-10, 10)
new_b = list(filter(lambda x: (x < 0 == 0), b))
print(new_b, "\n")

print("# 26*. Using the filter function, find the values that are common to the two lists:")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
new_common_list = list(filter(lambda x: x in list_1, list_2))
print(new_common_list)

