![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1

Napisz dekorator `rectifier`, który będzie dekorował/przerabiał funkcje jednoargumentowe zwracające liczby. 
Użycie dekoratora `rectifier` ma powodować, że zmodyfikowana funkcja nie będzie nigdy zwracała wartości ujemnych, 
zamiast nich zwracając zero.


## Zadanie 2

Napisz dekorator `stringify`, który będzie dekorował/przerabiał funkcje jednoargumentowe 
w taki sposób, żeby zwracana przez nie wartość była zawsze przerabiana na stringa.


## Zadanie 3

Napisz dekorator do funkcji zwracającej wartość logiczną wywołujący funkcję do czasu gdy zwróci True. 
Przetestuj na funkcji czytającej z wejścia i sprawdzającej czy użytkownik wpisał 'python'. Niech
dekorator jako argument przyjmuje liczbę całkowitą oznaczającą maksymalną liczbę prób wywołania
funkcji dekorowanej.