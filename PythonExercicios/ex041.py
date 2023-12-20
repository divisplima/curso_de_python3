"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos:JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

birth_year = int(input("Digite o ano de nascimento do atleta: "))
current_year = date.today().year
age = current_year - birth_year

if age <= 9:
    category = "MIRIM"
elif age <= 14:
    category = "INFANTIL"
elif age <= 19:
    category = "JUNIOR"
elif age <= 20:
    category = "SÊNIOR"
else:
    category = "MASTER"

print(f"O atleta tem {age} anos.")
print(f"Categoria: {category}")
