"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""
sex = str(input("Sexo (M/F): ")).strip().upper()[0]

while sex not in ['M', 'F']:
    print("Sexo inválido. Tente novamente.")
    sex = str(input("Sexo (M/F): ")).strip().upper()[0]
print(f"Sexo {sex} registrado com sucesso.")
