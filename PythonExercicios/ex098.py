"""
Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e 
realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada.
"""
from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1  

    print("-" * 30)
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")

    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=" ", flush=True)
            sleep(0.5)
            inicio += passo
    else:
        while inicio >= fim:
            print(inicio, end=" ", flush=True)
            sleep(0.5)
            inicio -= passo  

    print("\n" + "-" * 30)


def main():
    contador(1, 10, 1)

    contador(10, 0, 2)

    inicio = int(input("Digite o valor de início: "))
    fim = int(input("Digite o valor de fim: "))
    passo = int(input("Digite o valor do passo: "))
    contador(inicio, fim, passo)


if __name__ == "__main__":
    main()

