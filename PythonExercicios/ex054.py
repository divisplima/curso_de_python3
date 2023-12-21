"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

current_year = date.today().year
total_minors = total_adults = 0

for i in range(7):
    year_of_birth = int(input("Ano de nascimento: "))
    age = current_year - year_of_birth

    if age < 21:
        total_minors += 1
    else:
        total_adults += 1

print(f"{total_adults} atingiram a maioridade e {total_minors} não.")
