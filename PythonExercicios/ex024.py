"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
city_name = str(input("Nome da Cidade: ")).strip().upper().split()
print(city_name[0] == 'SANTO')

# Versão do Guanabara (foi feito algumas adaptações para que o código funcionasse).
print(city_name[0][:5] == 'SANTO')
