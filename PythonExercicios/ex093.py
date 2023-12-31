"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
import os

print("=" * 40)
print(f"{'APROVEITAMENTO DO JOGADOR':^40}")
print("=" * 40)

footballer = dict()
goals_scored = list()

footballer['name'] = str(input("Nome do Jogador: ")).strip()
footballer['matches played'] = int(input("Quantidades de partidas jogadas: "))

for i in range(footballer['matches played']):
    goals_scored.append(int(input(f"Quantos gols na {i+1}ª partida? ")))

footballer['goals scored'] = goals_scored
footballer['total goals'] = sum(footballer['goals scored'])

os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 40)
print(f"{'DETALHES DO JOGADOR':^40}")
print("=" * 40)

print(f"O jogador {footballer['name']} jogou {footballer['matches played']} partidas.")
for i, goals in enumerate(footballer['goals scored'], 1):
    print(f"    Na {i}ª partida, fez {goals} gol(s).")
print(f"Totalizando um total de {footballer['total goals']} gols.")
print("=" * 40)
