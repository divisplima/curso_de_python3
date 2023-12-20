"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
"""
print("Digite os comprimentos dos lados de um triângulo:")
side1 = float(input("Lado 1: "))
side2 = float(input("Lado 2: "))
side3 = float(input("Lado 3: "))

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print("Os lados formam um triângulo ", end='')
    if side1 == side2 == side3:
        print("equilátero.")
    elif side1 != side2 != side3 != side1:
        print("escaleno.")
    else:
        print("isósceles.")
else:
    print("Os lados não formam um triângulo.")
