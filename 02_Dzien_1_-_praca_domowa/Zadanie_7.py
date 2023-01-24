def histogram(numbers_list):
    i = ""
    try:
        for element in numbers_list:
            for el in range(element):
                i += "#"
            i += '\n'
    except TypeError:
        return None
    return i

print(histogram([2, 3, 5, 3, 9]))
print(histogram([2, 3, 'error', 3, 9]))
print(histogram([1, 2, 'error!']))
print(histogram([1, 2, 11, 5]))
