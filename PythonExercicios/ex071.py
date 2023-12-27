"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
valor será sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
# Define as notas disponíveis no caixa eletrônico
notes = [50, 20, 10, 1]

# Inicializa um dicionário para armazenar a quantidade de cada nota
note_counts = {note: 0 for note in notes}

print("=" * 40)
print(f"{'BANCO CEV':^40}")
print("=" * 40)

# Pergunta ao usuário qual valor será sacado
value = int(input("Qual valor você quer sacar? R$"))

# Verifica se a entrada do usuário é válida
if value < 0:
    print("Valor inválido. Por favor, insira um número inteiro positivo.")
else:
    # Calcula a quantidade de cada nota que será entregue
    for note in notes:
        while value >= note:
            note_counts[note] += 1
            value -= note

    # Imprime a quantidade de cada nota que será entregue
    for note, count in note_counts.items():
        if count > 0:
            print(f"Total de {count} cédulas de R${note}")
