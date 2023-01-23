def dogs_age(age):
    if age <= 2:
        result = age * 10.5
    elif age > 2:
        result = 2*10.5 + (age-2)*4
    return round(result, 2)

azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75
print(azor)
burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33
print(burek)