"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
tela o processo de cálculo do fatorial.
"""
def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    - num (int): O número para o qual calcular o fatorial.
    - show (bool, opcional): Se True, exibe o processo de cálculo na tela. Padrão é False.

    Retorna:
    int: O resultado do cálculo do fatorial.
    """
    if show:
        print(f"Calculando o fatorial de {num}: {num}! = ", end='')

    factorial = 1

    for i in range(num, 0, -1):
        factorial *= i
        if show:
            print(f"{i}", end='')
            if i > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')

    return factorial


def main():
    """
    Função principal que solicita ao usuário um número para calcular o fatorial
    e decide se mostrará ou não o processo de cálculo na tela.
    """
    num = int(input("Digite um número para calcular o fatorial: "))
    show_process = input("Deseja mostrar o processo de cálculo? (S/N): ").upper() == 'S'

    result = fatorial(num, show_process)

    print(result)


if __name__ == "__main__":
    main()
