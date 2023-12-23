"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" entre o número 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import os
import random
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

print(f"=" * 40)
print(f"{'JOGO DA ADIVINHAÇÃO v.2.0':^40}")
print(f"=" * 40)

computer_choice = random.randint(0, 10)
player_choice = int(input("De 0 a 10. Que número estou pensando? "))
attempts = 1

while player_choice != computer_choice:
    print("Processando...")
    sleep(1)
    
    if player_choice < computer_choice:
        print("Mais... tente outra vez.")
    else:
        print("Menos... Tente outra vez.")

    player_choice = int(input("De 0 a 10. Que número estou pensando? "))
    attempts += 1

print("VENCEU!")
print(f"Você precisou de {attempts} tentativas para acertar!")
print("=" * 40)
