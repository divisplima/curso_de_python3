"""
Crie um programa que faça o computador jogar jokenpô com você.
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')
from random import randint
from time import sleep

print("=" * 40)
print(f"{'JOKENPÔ GAME':^40}")
print("=" * 40)
print("Vamos jogar Jokenpô!")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

user_choice = int(input("Sua escolha: "))
computer_choice = randint(1, 3)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")

if user_choice == computer_choice:
    print("Empate!")
elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
    print("Você ganhou!")
else:
    print("Você perdeu!")

if computer_choice == 1:
    print("O computador escolheu Pedra.")
elif computer_choice == 2:
    print("O computador escolheu Papel.")
else:
    print("O computador escolheu Tesoura.")

print("=" * 40)
