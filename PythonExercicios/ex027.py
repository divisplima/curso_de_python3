"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeir e o último nome
separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
full_name = str(input("Nome completo: ")).strip().title()

name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[-1]

print(f"Primeiro nome: {first_name}.")
print(f"Último nome: {last_name}.")
