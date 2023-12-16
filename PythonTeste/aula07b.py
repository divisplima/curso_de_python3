num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponetiation = num1 ** num2

print(f"A soma é {addition}, a diferença é {subtraction}, o produto é {multiplication}", end=', ')
print(f"o quociente é {division:.2f}, o quociente (parte inteira da divisão) é {floor_division}", end=', ')
print(f"o resto é {modulus} e a potência é {exponetiation}.")
