def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def iterate_through(number):
    for element in range(1, number+1):
        print(element, is_even(element))

print(iterate_through(10))
