"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
"""
numbers = list()
running = True

while running:
    numbers.append(int(input("Digite um valor: ")))

    continue_input = None
    
    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

        if continue_input == 'N':
            running = False

position_5 = [position for position, number in enumerate(numbers) if number == 5]

print(f"Foram digitados {len(numbers)} valores.")
print(f"Lista em ordem decrescente: {numbers.sort(reverse=True)}.")

if 5 in numbers: 
    print(f"O 5 está na lista, nas posições {', '.join(map(str, position_5))}.")
else:
    print("O número 5 não está na lista.")
