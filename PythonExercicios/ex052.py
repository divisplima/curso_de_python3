"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

colour_code = {
    'clear': '\033[0m',
    'red': '\033[31m',
    'yellow': '\033[33m'
}

number = int(input("Digite um número: "))
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        print(colour_code['yellow'], end=' ')
        total += 1
    else:
        print(colour_code['red'], end=' ')
    
    print(i, end=' ')

if total == 2:
    print(f"{colour_code['clear']}\n{number} é um número primo.")
else:
    print(f"{colour_code['clear']}\n{number} não é um número primo.")
