"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados em ordem crescente.
"""
numbers = list()
running = True

while running:
    number = int(input("Insira um valor: "))

    if number not in numbers:
        numbers.append(number)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado. Não será adicionado.")

    continue_input = None
    
    while continue_input not in ['N', 'S']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if continue_input == 'N':
        running = False

numbers.sort()
print(f'Você digitou os valores: {numbers}')
