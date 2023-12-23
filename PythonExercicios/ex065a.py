"""
Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
# bing's version
numeros = []
continuar = 'S'

while continuar == 'S':
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    continuar = input("Deseja continuar? [S/N] ").upper()

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"A média dos números digitados é {media}.")
print(f"O maior número digitado foi {maior}.")
print(f"O menor número digitado foi {menor}.")
