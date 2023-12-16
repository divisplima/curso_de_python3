"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um númro: 6.127
O número 6.127 tem a parte inteira 6.
"""
from math import trunc

num = float(input("Digite um número: "))
print(f"O número {num} tem a parte inteira {trunc(num)}.")  # Método 1

print(f"O número {num} tem a parte inteira {int(num)}.")    # Método 2
