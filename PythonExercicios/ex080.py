"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já
na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""
numbers = list()

for i in range(5):
    number = int(input("Digite um valor: "))

    if len(numbers) == 0 or number > numbers[-1]:
        numbers.append(number)
        print("Adicionado ao final da lista.")
    else:
        for j in range(len(numbers)):
            if number <= numbers[j]:
                numbers.insert(j, number)
                print(f"Adicionado na posição {j} da lista.")
                break

print(f'Os valores digitados em ordem são: {numbers}')
