'''
Napisz grę: "Papier, Kamień, Nożyce"
Gra ma przyjmować z klawiatury
    1 - kamień
    2 - nożyce
    3 - papier
Następnie ma losować co wybrał komputer i ogłaszać werdykt.
'''

import random

stone = 1
scissors = 2
paper = 3

my_choice = True

while my_choice:
    try:
        my_choice = int(input('Wybierz kamień (wciśnij 1), nożyce (wciśnij 2), lub papier (wciśnij 3)'))

        if my_choice in range(0, 4):
            computers_choice = random.randint(1, 3)

            print(computers_choice)

            if my_choice == computers_choice:
                    print('Remis.')
            elif my_choice == 1 and computers_choice == 2:
                print('Wygrałeś!')
            elif my_choice == 1 and computers_choice == 3:
                print('Przegrałeś!')
            elif my_choice == 2 and computers_choice == 1:
                print('Przegrałeś!')
            elif my_choice == 2 and computers_choice == 3:
                print('Wygrałeś!')
            elif my_choice == 3 and computers_choice == 1:
                print('Wygrałeś!')
            elif my_choice == 3 and computers_choice == 2:
                    print('Przegrałeś!')
        else:
            print('Wybrałeś błędną wartość!')
    except ValueError:
        print("To nie jest liczba! Spróbuj ponownie.")
