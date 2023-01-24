def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_2(n):
    result = [1, 1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])
    return result[-1]

print(fib(3))  # 2
print(fib_2(4))  # 3
print(fib(8))  # 21
print(fib_2(16))  # 987
