def phone(number):
    numbers_list = [252330210, 151226792, 717453535, 676809930, 925147727, 551396640, 569159153]
    if number in numbers_list:
        return number
    else:
        raise Exception('Nie ma takiego numeru')

print(phone(252330210))
print(phone(815720735))
