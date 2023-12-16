"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
number = int(input("Digite um número: "))

double = number * 2
triple = number * 3
square_root = number ** 0.5

print(f"""O dobro de {number} é {double}.
O triplo de {number} é {triple}.
A raiz quadrada de {number} é {square_root:.2f}.""")
