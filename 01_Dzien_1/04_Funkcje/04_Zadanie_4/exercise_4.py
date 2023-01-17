# write the function from exercise 4 here
def convert_to_usd(zlotys):
    return round(zlotys / 3.85, 2)

# the lines below will test your function:
print("385EUR = ", convert_to_usd(385), "USD")
print("100EUR = ", convert_to_usd(100), "USD")