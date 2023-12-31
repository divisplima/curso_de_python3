"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.
"""
import random
from time import sleep
from operator import itemgetter

results = dict()

for player in range(1, 5):
    results[f'player {player}'] = random.randint(1, 6)

for player, score in results.items():
    print(f"{player} tirou: {score} no dado.")
    sleep(0.5)

print(f"\n{'RESULTADO':=^40}")

sorted_results = sorted(results.items(), key=itemgetter(1), reverse=True)

for rank, (player, score) in enumerate(sorted_results, start=1):
    print(f"{rank}º lugar está o {player} que tirou {score} pontos.")
    sleep(0.5)
