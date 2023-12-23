"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
"""
first_term = int(input("Primeiro termo: "))
common_difference = int(input("Razão: "))
i = 1

while i <= 10:
    term = first_term + (i - 1) * common_difference
    i += 1
    print(term, end=' ')
