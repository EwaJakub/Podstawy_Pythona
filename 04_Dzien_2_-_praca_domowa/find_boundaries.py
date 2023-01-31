def find_boundaries(numbers_list):
    checked_list = [num for num in numbers_list if isinstance(num, (float, int))]
    print(checked_list)
    return (min(checked_list), max(checked_list))

b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)  # (-1, 5)

b = find_boundaries([0, 2, "a kuku!", 10])
print(b)  # (0, 10)
