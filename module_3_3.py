def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)

print_params(1, 'строка', True)

print_params(True, 'строка', 1)

print_params('строка', True, 1)

print_params()

print_params(b = 25)

print_params(c = [1, 2, 3])


values_list = [1, 2, 'строка']
values_dict = {'a' : 4, 'b' : 0, 'c' : False}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)