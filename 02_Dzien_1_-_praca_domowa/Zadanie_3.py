def circle_circuit(a, pi=3.14):
    return round(2 * pi * (a/2), 6)

dia = 5
result = circle_circuit(dia)
print(f"Obwód koła o średnicy {dia} wynosi {result}.")