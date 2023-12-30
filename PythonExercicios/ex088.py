"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
"""
import random
from time import sleep

print("=" * 40)
print(f"{'PALPITES DA MEGA SENA':^40}")
print("=" * 40)

num_games = int(input("Quantos jogos você quer gerar? "))

print("\nGerando palpites:")
for i in range(1, num_games + 1):
    game = random.sample(range(1, 61), 6)
    sleep(0.5)
    print(f"Jogo {i}: {', '.join(map(str, sorted(game)))}")
print("=" * 40)
