"""
Crie um programa que tenha a função leiaint(), que vai funcionar semelhante a função input() do Python, só
fazendo a validação para aceitar apenas um valor numérico

Ex.: leiaint("Digite um número: ")
"""
def leiaint(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Por favor, digite um valor numérico válido.")


def main():
    numero = leiaint("Digite um número: ")
    print(f"Você digitou o número: {numero}")


if __name__ == "__main__":
    main()
