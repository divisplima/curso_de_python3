"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
number = int(input("Digite um número: "))
counter = number
factorial = 1
print(f"{number}! = ", end='')

while counter > 0:
    print(counter, end='')
    print(f" x " if counter > 1 else " = ", end='')
    factorial *= counter
    counter -= 1
print(factorial)
