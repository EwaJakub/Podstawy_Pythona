import random

def average(f):
    def inner(x):
        func = f(x)
        return sum(func)/len(func)
    return inner

@average
def random_average(n):
    return [random.randint(1, 100) for _ in range(n)]

print(random_average(5))