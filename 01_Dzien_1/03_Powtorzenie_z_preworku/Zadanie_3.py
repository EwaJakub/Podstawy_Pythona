from random import randint

size = randint(3, 9)

print(f"Size: {size}")

for element in range(size):
    for el in range(element):
        print('*', end="") # w ramach każdego wiersza dla zakresu elementów dodaje *, bez przenoszenia do kolejnej linii
    print('*')  # dodaje * do każdego iterowanego wiersza

# sposób 2
for element in range(size):
    i = '*'
    for el in range(element):
        i += '*'
    print(i)