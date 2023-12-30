"""
Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
"""
general_data = list()
heavier_weight = list()
lighter_weight = list()

running = True

while running:
    personal_data = list()

    personal_data.append(str(input("Nome: ")).strip())
    personal_data.append(float(input("Peso (Kg): ")))

    if personal_data[1] <= 70.0:
        lighter_weight.append(personal_data.copy())
    elif personal_data[1] >= 100.0:
        heavier_weight.append(personal_data.copy())

    general_data.append(personal_data.copy())

    continue_input = None

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

        if continue_input == 'N':
            running = False

print("Dados cadastrados:")
for person in general_data:
    print(f"Nome: {person[0]}, Peso: {person[1]} Kg")

print(f"\nTotal de {len(general_data)} pessoas cadastradas.")

if lighter_weight:
    print("\nPessoas mais leves:")
    for person in lighter_weight:
        print(f"Nome: {person[0]}, Peso: {person[1]} Kg")

if heavier_weight:
    print("\nPessoas mais pesadas:")
    for person in heavier_weight:
        print(f"Nome: {person[0]}, Peso: {person[1]} Kg")
