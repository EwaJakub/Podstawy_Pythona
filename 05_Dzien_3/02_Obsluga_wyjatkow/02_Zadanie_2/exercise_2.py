from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    try:
        str_num = input("Enter number:")
        num = int(str_num)
        if num == rnd:
            print("Great!")
            guessed = True
        elif num not in range(1, 11):
            raise UserWarning
        else:
            print("Wrong!")
    except ValueError:
        print("Value is incorrect!")
    except UserWarning:
        print("Value out of range")
