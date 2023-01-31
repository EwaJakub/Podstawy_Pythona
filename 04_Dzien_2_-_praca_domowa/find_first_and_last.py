def find_first_and_last(collection):
    result = (collection[0], collection[-1])
    print(type(result))
    return result

print(find_first_and_last([2, 4, 3, 8, 9]))  # (2, 9)
print(find_first_and_last(["Ania", 4, "Kasia", 8, 9]))  # ('Ania', 9)
