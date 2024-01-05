def aumentar(preco=0.0, taxa=0, formato=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formato == False else moeda(resposta)


def diminuir(preco=0.0, taxa=0, formato=False):
    resposta = preco - (preco * taxa/100)
    return resposta if formato == False else moeda(resposta)


def dobro(preco=0.0, formato=False):
    resposta = preco * 2
    return resposta if formato == False else moeda(resposta)


def metade(preco=0.0, formato=False):
    resposta = preco / 2
    return resposta if formato == False else moeda(resposta)


def moeda(preco=0.0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.', ',')


def resumo(preco=0.0, taxaa=10, taxar=5):
    print("=" * 30)
    print("RESUMO DO VALOR".center(30))
    print("=" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}")
    print(f"{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}")
    print("=" * 30)