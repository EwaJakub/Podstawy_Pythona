from random import randint

def d6(num):
    num_list = [randint(1, 6) for _ in range(0, num)]
    print(num_list)
    return sum(num_list)

print(d6(8))
