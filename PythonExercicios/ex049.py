"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora 
utilizando o laço for.
"""
number = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{number} * {i:2} = {number * i}")
