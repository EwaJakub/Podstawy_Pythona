from random import randint

rows = randint(5, 15)
columns = randint(5, 15)

print(f"Rows: {rows}")
print(f"Columns: {columns}")

for element in range(rows):
    print('*' * columns)

# other solution: solution = (columns * "*" + "\n") * rows
