"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar desconsidere-o.
"""
even = 0

for i in range(6):
    number = int(input("Digite um número: "))

    if number % 2 == 0:
        even += number

print(f"A soma de todos os valores pares digitados é {even}.")
