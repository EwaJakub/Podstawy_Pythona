def chessboard(n=8):
    i = ""
    for element in range(1, n+1):
        if element % 2 != 0:
            if n % 2 == 0:
                i += (int((n/2)) * "# " + "\n")
            elif n % 2 != 0:
                i += (int((n/2)) * "# " + "#" + "\n")
        elif element % 2 == 0:
            i += (int((n/2)) * " #" + "\n")
    return i

print(chessboard())
print(chessboard(7))
print(chessboard(6))
print(chessboard(3))