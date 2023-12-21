"""
Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
import os

average_age_group = oldest_man_age = count_women_under_20 = 0
oldest_man_name = ''

for i in range(1, 5):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 40)
    print(f"{'CADASTRO DE PESSOAS':^40}")
    print("=" * 40)

    name = str(input("Nome: ")).strip().upper()
    age = int(input("Idade: "))
    sex = str(input("Sexo (M/F): ")).strip().upper()

    average_age_group += age

    if sex[0] == 'M' and oldest_man_age < age:
        oldest_man_age = age
        oldest_man_name = name

    if sex[0] == 'F' and age < 20:
        count_women_under_20 += 1

print("=" * 40)
print(f"A média de idade do grupo é de {average_age_group / i} anos.")
print(f"O nome do homem mais velho é {oldest_man_name} e tem {oldest_man_age} anos.")
print(f"Há, no total, {count_women_under_20} mulheres com idade abaixo de 20.")
