heroes = ["Harry", "Ron", "Hermione"]
while True:
    try:
        x = input("Wprowadź indeks: ")
        index = int(x)
        print(heroes[index])
        break
    except ValueError:
        print("To nie jest liczba!"
              "Spróbuj ponownie.")
    except IndexError:
        print("W tablicy heroes nie ma elementu o tym indeksie!")
