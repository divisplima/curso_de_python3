"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
import os

os.system('cls' if os.name =='nt' else 'clear')

colour_codes = {
    'red': '\033[31m',
    'clear': '\033[0m'
}

print("=" * 40)
print(f"{'CONVERSOR DE BASES NUMÉRICAS':^40}")
print("=" * 40)

decimal_number = int(input("Digite um número inteiro: "))

print("-" * 40)
print("Escolha a base de conversão:")
print("1 - Conversão para binário")
print("2 - Conversão para octal")
print("3 - Conversão para hexadecimal")

conversion_base = int(input("Opção: "))

if conversion_base == 1:
    print(f"O número {decimal_number} em binário é: {colour_codes['red']}{bin(decimal_number)[2:]}{colour_codes['clear']}.")
elif conversion_base == 2:
    print(f"O número {decimal_number} em octal é: {colour_codes['red']}{oct(decimal_number)[2:]}{colour_codes['clear']}.")
elif conversion_base == 3:
    print(f"O número {decimal_number} em hexadecimal é: {colour_codes['red']}{hex(decimal_number)[2:]}{colour_codes['clear']}")
else:
    print("Opção inválida. Escolha 1, 2 ou 3 para a conversão.")
