"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual delas é maior.
"""
from time import sleep

def maior(*numbers):
    if not numbers:
        print("Nenhum valor foi informado.")
        return

    print("\nAnalisando os valores:")
    for number in numbers:
        print(number, end=' ', flush=True)
        sleep(0.5)

    print(f"\nForam analisados {len(numbers)} valores ao todo.")
    print(f"O maior número analisado foi: {max(numbers)}.\n")


def main():
    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()


if __name__ == "__main__":
    main()
