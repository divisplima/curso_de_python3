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
