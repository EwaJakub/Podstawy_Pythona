def suma(numbers):
    return sum(numbers)

def suma_2(numbers):
    i = 0
    for number in numbers:
        i += number
    return i


print(suma([1, 2.8, 4, 9]))
print(suma_2([1, 2.8, 4, 9]))
