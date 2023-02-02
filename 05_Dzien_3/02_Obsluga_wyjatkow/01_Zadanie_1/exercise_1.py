def safe_get(l, index):
    try:
        return l[index]
    except (IndexError, TypeError):
        return None


print(safe_get([2, 5, 2, 5, 9], 'referf'))
print(safe_get([2, 4, 5, 6, 8], 3))
print(safe_get([2, 4, 5, 6, 8], 10))
print(safe_get([2, "a", 5, 6, 8], 1))
print(safe_get([2, 4, 5, 6, 8], "a"))