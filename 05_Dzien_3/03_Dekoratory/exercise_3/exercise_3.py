def check_if_true(f):
    def inner(x):
        i = 1
        print(x)
        while f(x) is not True and i in range(0, x):
            i += 1
        return 'this is the end'
    return inner


@check_if_true
def input_value(x):
    result = input('Wpisz "python"')
    if result == 'python':
        return True
    else:
        return False


print(input_value(4))
