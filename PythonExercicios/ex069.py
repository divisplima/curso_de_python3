"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
"""
import os

over_18_count = male_count = female_under_20_count = 0


continue_input = 'S'
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 40)
    print(f"{'CADASTRE UMA PESSOA':^40}")
    print("=" * 40)

    age = int(input("Idade: "))
    sex = ''

    while sex not in ['M', 'F']:
        sex = str(input("Sexo [M/F]: ")).strip().upper()[0]
    
    if age > 18:
        over_18_count += 1

    if sex == 'M':
        male_count += 1
    
    if age < 20 and sex == 'F':
        female_under_20_count += 1

    continue_input = ''

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    
    if continue_input == 'N':
        break

print("=" * 40)
print(f"Ao todo {over_18_count} pessoas tem mais de 18 anos.")
print(f"Há {male_count} homens cadastrados.")
print(f"Há {female_under_20_count} mulheres com menos de 20 anos cadastradas.")
