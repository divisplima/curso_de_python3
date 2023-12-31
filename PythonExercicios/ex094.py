"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média.
"""
import numpy as np

people_data = list()
personal_data = dict()

running = True

while running:
    personal_data['name'] = str(input("Nome: ")).strip()
    personal_data['sex'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    personal_data['age'] = int(input("Idade: "))
    
    people_data.append(personal_data.copy())

    continue_input = None

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    
        if continue_input == 'N':
            running = False

ages = np.array([person['age'] for person in people_data])

average_age = np.mean(ages)

women_list = [person['name'] for person in people_data if person['sex'] == 'F']
above_average_age_list = [person['name'] for person in people_data if person['age'] > average_age]

print(f"\nTotal de pessoas cadastradas: {len(people_data)}")
print(f"Média de idade do grupo: {average_age:.2f} anos")
print(f"Lista de mulheres: {', '.join(women_list)}")
print(f"Pessoas com idade acima da média: {', '.join(above_average_age_list)}")
