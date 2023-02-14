def div(num1, num2):
    return [num for num in range(num1, num2+1) if num%2 == 0 and num %3 != 0 and num != 0]

result = div(0, 20)
print(result)
