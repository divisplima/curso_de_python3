"""
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela
algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""
from moeda import *

def main():
    p = float(input("Digite o preço: R$"))
    resumo(p)


if __name__ == "__main__":
    main()
