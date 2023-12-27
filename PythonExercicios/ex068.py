"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
"""
import random

# Define um dicionário para os códigos de cores
colour_code = {
    'clear': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m' 
}

# Imprime o cabeçalho do programa
print("=" * 40)
print(f"{'JOGO DO PAR OU ÍMPAR':^40}")

# Inicializa o contador de vitórias
total_win = 0

# Inicia um loop infinito para o jogo
while True:
    print("=" * 40)

    # Solicita ao jogador que insira um número e escolha par ou ímpar
    player_number = int(input("Digite um número: "))
    player_choice = str(input("PAR ou ÍMPAR [P/I]? ")).strip().upper()[0]

    # Verifica se a escolha do jogador é válida
    while player_choice not in ['P', 'I']:
        player_choice = str(input("PAR ou ÍMPAR [P/I]: ")).strip().upper()[0]

    # Gera um número aleatório para o computador
    computer_number = random.randint(0, 10)

    # Calcula a soma do número do jogador e do computador
    total = player_number + computer_number

    # Determina se a soma é par ou ímpar
    if total % 2 == 0:
        even_or_odd = 'PAR'
    else:
        even_or_odd = 'ÍMPAR'

    # Imprime os resultados
    print(f"Você jogou {player_number} e o Computador {computer_number}. Total de {total} e deu {even_or_odd}.")

    # Verifica se o jogador ganhou ou perdeu
    if (even_or_odd == 'PAR' and player_choice == 'P') or (even_or_odd == 'ÍMPAR' and player_choice == 'I'):
        print(colour_code['green'])
        print("JOGADOR VENCEU!")
        print(colour_code['clear'])

        total_win += 1 # Incrementa do número de vitórias
    else:
        print(colour_code['red'])
        print("JOGADOR PERDEU!")
        print(colour_code['clear'])
        print("=" * 40)
        break  # Termina o jogo se o jogador perdeu
print(f"Você venceu {total_win} vezes.")
