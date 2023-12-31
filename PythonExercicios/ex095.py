"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.
"""
print("=" * 40)
print(f"{'APROVEITAMENTO DE JOGADORES':^40}")
print("=" * 40)

players = list()

running = True
while running:
    footballer = dict()  # Cria um novo dicionário para cada jogador
    footballer['name'] = str(input("Nome do Jogador: ")).strip()
    footballer['matches played'] = int(input("Quantidade de partidas jogadas: "))

    goals_scored = list()  # Reinicializa a lista para cada jogador

    for i in range(footballer['matches played']):
        goals_scored.append(int(input(f"Quantos gols na {i+1}ª partida? ")))

    footballer['goals scored'] = goals_scored
    footballer['total goals'] = sum(footballer['goals scored'])

    players.append(footballer.copy())

    continue_input = None

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

        if continue_input == 'N':
            running = False

print("=" * 40)
print(f"{'ID':<4}{'NOME':<15}{'PARTIDAS':<15}{'GOLS':<15}")
print("=" * 40)
for idx, player in enumerate(players):
    print(f"{idx:<4}{player['name']:<15}{player['matches played']:<15}{player['total goals']:<15}")
print("=" * 40)

running = True
while running:
    search = int(input("Qual jogador você quer detalhes (999 para sair)? "))

    if search == 999:
        running = False
    elif search >= len(players) or search < 0:
        print(f"ERRO. Não existe jogador com o código {search}.")
    else:
        print("=" * 40)
        print(f"LEVANTAMENTO DO JOGADOR {players[search]['name'].upper()}:")

        for index, goals in enumerate(players[search]['goals scored']):
            print(f"    No jogo {index+1} fez {goals} gol(s).")
        print(f"Totalizando {players[search]['total goals']} gol(s).")
print("=" * 40)
