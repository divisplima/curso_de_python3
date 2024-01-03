"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente.
"""
def ficha(footballer='null', goals=0):
    print(f"O jogador {footballer} fez {goals} gol(s) no campeonato.")


def main():
    name = str(input("Jogador: ")).strip()
    goals = str(input("Gol(s): ")).strip()

    if goals.isnumeric():
        goals = int(goals)
    else:
        goals = 0

    if name.strip() == '':
        ficha(goals=goals)
    else:
        ficha(footballer=name, goals=goals)


if __name__ == "__main__":
    main()
