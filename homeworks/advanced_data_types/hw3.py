
# 1. Define the id of next variables:'
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.'
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches.'.format(3, 2))

# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches.'.format(2, 3))

# 7. By using keyword arguments into the curly braces.
print('Anna has {apples} apples and {peaches} peaches.'.format(apples=3, peaches=2))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {1:5} apples and {0:3} peaches.'.format(2, 3))

# 9. With f-strings and variables
a = 3
p = 2
print(f'Anna has {a} apples and {p} peaches.')

# 10. With % operator
print('Anna has %d apples and %d peaches.' % (3, 2))

# 11*. With variable substitutions by name (hint: by using dict)
apples = 3
peaches = 2
data_dict = {"apples": apples, "peaches": peaches}
print('Anna has %(apples)d apples and %(peaches)d peaches.' % data_dict)

