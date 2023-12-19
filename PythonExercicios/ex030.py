"""
Crie um programa que leia um número inteiro e moste na tela se ele é PAR ou ÍMPAR.
"""
number = int(input("Digite um número qualquer: "))

if number % 2 == 0:
    print(f"{number} é um número PAR.")
else:
    print(f"{number} é um número ÍMPAR.")
