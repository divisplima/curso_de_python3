"""
Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um módulo chamado dado. Crie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para
aceitar apenas valores que sejam monetários.
"""
from ex112.utilidadesCeV import moeda 
from ex112.utilidadesCeV import dado

def main():
    p = dado.leiaDinheiro("Digite o preço: R$")
    moeda.resumo(p)


if __name__ == "__main__":
    main()
