"""
Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado.
"""
from moeda import *

def main():
    valor = float(input("Preço: R$"))
    print(f"Valor do produto: {moeda(valor)}"
          f"\nAumento: {moeda(aumentar(valor, taxa=5))}"
          f"\nDobro: {moeda(dobro(valor))}")


if __name__ == "__main__":
    main()
