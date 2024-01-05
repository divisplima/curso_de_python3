"""
Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(), diminuir(), dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from moeda import *

def main():
    valor = float(input("Preço: R$"))
    print(f"Valor do produto: R${valor:.2f}"
          f"\nAumento: R${aumentar(valor, taxa=5):.2f}"
          f"\nDobro: R${dobro(valor):.2f}")


if __name__ == "__main__":
    main()
