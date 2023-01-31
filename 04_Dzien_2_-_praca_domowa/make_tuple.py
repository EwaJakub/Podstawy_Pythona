def make_tuple(a, b, c=3, d=4):
    result = (a, b, c, d)
    return result

a = make_tuple("mama", "tata")
print(a)  # ('mama', 'tata', 3, 4)

a = make_tuple(0, 0, 0, 0)
print(a)  # (0, 0, 0, 0)
