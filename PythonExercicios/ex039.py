"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

Desafio: Perguntar o sexo da pessoa e dizer se ela precisa ou não fazer o alistamento militar obrigatório.
"""
from datetime import date

current_year = date.today().year
birth_year = int(input("Digite o ano do seu nascimento: "))
sex = str(input("Qual é o seu sexo (MF)? ")).strip().upper()
age = current_year - birth_year

print(f"Quem nasceu em {birth_year} tem {age} anos em {current_year}.")
if sex == 'M':
    if age < 18:
        balance = 18 - age
        print(f"Ainda faltam {balance} anos para o alistamento.")
        enlistment_year = current_year + balance
        print(f"Seu alistamento será em {enlistment_year}.")
    elif age == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")
    else:
        balance = age - 18
        print(f"Você já deveria ter se alistado há {balance} anos.")
        enlistment_year = current_year - balance
        print(f"Seu alistamento foi em {enlistment_year}.")
elif sex == 'F':
    print("Você não precisa fazer o alistamento obrigatório.")
else:
    print('Sexo inválido. Tente novamente.')
