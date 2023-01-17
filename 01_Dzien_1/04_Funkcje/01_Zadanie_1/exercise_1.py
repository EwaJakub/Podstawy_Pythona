# write the function from exercise 1 here
def square(num):
    return num ** 2

def square_print(num):
    print(num ** 2)

# the lines below will test your function:
print("2 squared is:", square(2))  # should be 4
print("16^2=", square(16))  # should be 256
print("256 to the 2nd power =", square(256))  # should be 65536

a = square(10) + 10
print(a)
b = square_print(10) + 10 # returned value is None, it can't be a sum with int
print(b)