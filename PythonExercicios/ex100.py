"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.
"""
import random
from time import sleep

def sorteio(lista):
    print("Sorteando cinco valores da lista:")

    for _ in range(5):
        number = random.randint(1, 10)
        lista.append(number)
        print(f"{number} ", end='', flush=True)
        sleep(0.3)
    print("PRONTO!")
    sleep(0.5)  # Adiciona uma pausa adicional no final do sorteio


def soma_par(lista):
    soma = sum(number for number in lista if number % 2 == 0)
    print(f"A soma dos valores pares é igual a {soma}.")


def main():
    numeros = []
    sorteio(numeros)
    sleep(0.5)  # Adiciona uma pausa antes de chamar a função soma_par
    soma_par(numeros)


if __name__ == "__main__":
    main()
