"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista
que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
"""
numbers = [[], []]

for i in range(7):
    number = int(input(f"Digite o {i+1}º valor: "))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()

print(f"Pares: {numbers[0]}.")
print(f"Ímpares: {numbers[1]}.")
