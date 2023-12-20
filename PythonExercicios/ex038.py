"""
Escreva um programa que leia dois número inteiros e compare-os, mostrando na sua tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
number1 = int(input("Primeiro número: "))
number2 = int(input("Segundo número: "))

if number1 > number2:
    print("O primeiro valor é maior.")
elif number1 == number2:
    print("Não existe valor maior, os dois são iguais.")
else:
    print("O segundo valor é maior.")
