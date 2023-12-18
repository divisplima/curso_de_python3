"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""
import os

os.system('cls')

full_name = str(input("Nome completo: ")).strip()

print(f"{full_name.upper()}")
print(f"{full_name.lower()}")

total_letters = len(''.join(full_name.split()))
first_name_letters = len(full_name.split()[0])

print(f"Qtd. total de letras: {total_letters}.")
print(f"Qtd. letras no primeiro nome: {first_name_letters}.")

# Feito pelo Guanabara
print(f"Qtd. total de letras: {len(full_name) - full_name.count(' ')}.")
print(f"Qtd. letras no primeiro nome: {full_name.find(' ')}.")
