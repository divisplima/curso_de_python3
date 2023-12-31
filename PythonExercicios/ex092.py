"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

worker_data = dict()

current_year = datetime.now().year

worker_data['name'] = str(input("Nome: ")).strip()
worker_data['birth year'] = int(input("Ano de nascimento: "))
worker_data['age'] = current_year - worker_data['birth year']
worker_data['ctps'] = int(input("Carteira de trabalho (0 não tem): "))

if worker_data['ctps'] != 0:
    worker_data['year of employment'] = int(input("Ano de contratação: "))
    worker_data['salary'] = float(input("Salário: "))
    
    work_time = current_year - worker_data['year of employment']
    worker_data['retirement age'] = worker_data['age'] + (35 - work_time)

print(f"\n{'DADOS DO TRABALHADOR':=^40}")
print(f"Nome: {worker_data['name']}")
print(f"Ano de nascimento: {worker_data['birth year']}")
print(f"idade: {worker_data['age']}")

if worker_data['ctps'] != 0:
    print(f"Carteira de Trabalho: {worker_data['ctps']}")
    print(f"Ano de contratação: {worker_data['year of employment']}")
    print(f"Salário: R${worker_data['salary']:.2f}")
    print(f"Vai se aposentar aos {worker_data['retirement age']} anos.")
else:
    print("Este trabalhador não possui carteira de trabalho.")
print(f"\n{'FIM DO PROGRAMA':=^40}")