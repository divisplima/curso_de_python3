"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e ímpares digitados respectivamente.

No final, mostre o conteúdo das trê listas geradas.
"""
numbers = []
even_numbers = []
odd_numbers = []

while True:
    numbers.append(int(input("Digite um valor: ")))

    continue_input = None

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if continue_input == 'N':
        break

for number in numbers:
    target_list = even_numbers if divmod(number, 2)[1] == 0 else odd_numbers
    target_list.append(number)

print(f"Lista principal: {', '.join(map(str, numbers))}")
print(f"Lista pares: {', '.join(map(str, even_numbers))}")
print(f"Lista ímpares: {', '.join(map(str, odd_numbers))}")
