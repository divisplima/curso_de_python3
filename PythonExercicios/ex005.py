"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
number = int(input("Insira um número: "))

predecessor = number - 1
successor = number + 1

print(f"O antecessor de {number} é {predecessor} e o sucessor é {successor}.")
