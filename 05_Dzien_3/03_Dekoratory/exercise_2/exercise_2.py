def stringify(f):
    def inner(x):
        return str(f(x))
    return inner

@stringify
def value(a):
    return a

print(isinstance(value('a'), str))
print(isinstance(value(2), str))
