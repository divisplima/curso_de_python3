"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
heaviest_weight = lightest_weight = 0

for i in range(1, 6):
    person_weight = float(input(f"Peso da {i}ª pessoa: "))

    if i == 1:
        heaviest_weight = lightest_weight = person_weight
    else:
        if person_weight > heaviest_weight:
            heaviest_weight = person_weight  

        if person_weight < lightest_weight:
            lightest_weight = person_weight  

print(f"O maior peso registrado é de {heaviest_weight}Kg.")
print(f"O menor peso registrado é de {lightest_weight}Kg.")
