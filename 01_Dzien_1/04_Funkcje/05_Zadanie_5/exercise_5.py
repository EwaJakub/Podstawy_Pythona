'''
     (F - 32) * 5
C =  ------------
          9
gdzie:

    C – temperatura w stopniach Celsjusza,
    F – temperatura w stopniach Fahrenheita.
'''


def to_celsius(fahrenheit):
    return round(((fahrenheit - 32) * 5)/9, 2)

print("100 stopni Fahrenheita to", to_celsius(100), "C")