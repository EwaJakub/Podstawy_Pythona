def divide(a, b):
    try:
        if int(a) < 0 or int(b) < 0:
            raise ValueError
        else:
            return int(a)/int(b)
    except (ValueError, ZeroDivisionError):
        return None

print(divide('a', 4))  # None
print(divide(2, 0))  # None
print(divide(-2, 2))  # None
print(divide(2, 2))  # 1.0
