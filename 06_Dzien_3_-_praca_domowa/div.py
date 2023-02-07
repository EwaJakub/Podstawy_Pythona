def div():
    result = False
    while result is not True:
        try:
            input_value_1 = int(input('Podaj liczbę:'))
            input_value_2 = int(input('Podaj liczbę:'))
            result = input_value_1/input_value_2
            break  # jeśli nie otrzymamy błędu warości pętla się zatrzyma
        except (ValueError, ZeroDivisionError):
            print('please try again, give two numbers')
    return result


print(div())
