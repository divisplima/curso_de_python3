"""
Modifique as funções que foram criadas no DESAFIO 107 para que aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvida no DESAFIO 108.
"""
from moeda import *

def main():
    p = float(input("Digite o preço: R$"))
    print(f"A metade de {moeda(p)} é {metade(p, True)}")



if __name__ == "__main__":
    main()
