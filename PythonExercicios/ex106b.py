def ajuda(command):
    """
    Exibe o manual de uma função ou biblioteca utilizando a função help do Python.

    :param command: O nome da função ou biblioteca para a qual o manual será exibido.
    :type command: str
    """
    titulo(f"Acessando o manual do comando '{command}'", cor=2)
    help(command)


def titulo(texto, cor=0):
    """
    Imprime um título formatado no console.

    :param texto: O texto a ser exibido como título.
    :type texto: str
    :param cor: O código da cor ANSI para o título (opcional, padrão é 0 para branco).
    :type cor: int
    """
    cores = [
        '\033[0m',  # Resetar cor
        '\033[31m',  # Vermelho
        '\033[32m'   # Verde
    ]
    print(f"{cores[cor]}~" * (len(texto) + 4))
    print(f"{cores[cor]}{texto:^{len(texto) + 4}}")
    print(f"{cores[cor]}~" * (len(texto) + 4))


def main():
    """
    Função principal que executa a central de ajuda PyHELP.

    Solicita ao usuário um comando (função ou biblioteca) e exibe o manual correspondente.
    O programa encerra quando o usuário digita 'FIM'.
    """
    titulo("CENTRAL DE AJUDA PyHELP", cor=2)

    command = None

    while True:
        command = input("Função ou biblioteca (ou 'FIM' para encerrar): ")
        
        if command.upper() == 'FIM':
            break
        else:
            ajuda(command)

    titulo("FIM DO PROGRAMA", cor=1)


if __name__ == "__main__":
    main()
