def rectifier(f):
    def inner(x):
        if f(x) > 0:
            return f(x)
        elif f(x) < 0:
            return 0
    return inner

@rectifier
def one_arg_func(x):
    return x

print(one_arg_func(30))  # 30
print(one_arg_func(105))  # 105
print(one_arg_func(5))  # 5
print(one_arg_func(-5))  # 0


