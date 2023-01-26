def create_list(arg_1, arg_2):
    return [arg_1 if el % 2 != 0 else arg_2 for el in range(1, 9)]


my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
print(my_list)
my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]
print(my_list_2)
