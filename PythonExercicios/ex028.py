"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import os
from random import randint
from time import sleep


# Clear the console screen using 'cls' on Windows, or 'clear' on Unix/Linux
# os.system('clear')
os.system('cls' if os.name == 'nt' else 'clear')

print(f"=" * 40)
print(f"{'JOGO DA ADIVINHAÇÃO v.1.0':^40}")
print(f"=" * 40)

computer_choice = randint(0, 5)
player_choice = int(input("De 0 a 5. Que número estou pensando? "))

print("Processando...")
sleep(1)

if computer_choice == player_choice:
    print("VENCEU!")
else:
    print(f"PERDEU! Pensei no número {computer_choice}.")

print("=" * 40)
