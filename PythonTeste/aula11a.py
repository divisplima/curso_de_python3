print("\033[31mOlá, Mundo!\033[0m")         # Texto em vermelho
print("\033[31;43mOlá, Mundo!\033[0m")      # Texto em vermelho com o fundo amarelo
print("\033[1;31;43mOlá, Mundo!\033[0m")    # Texto em negrito, vermelho e com o fundo amarelo
print("\033[4;30;45mOlá, Mundo!\033[0m")    # Sublitado, com letra branca e fundo roxo
print("\033[7;30mOlá, Mundo!\033[0m")       # Fundo branco, letra preta

cores = {
    'limpa':'\033[0m',
    'azul': '\033[34m'
}

print(f"{cores['azul']}Olá, Mundo!{cores['limpa']}")
