"""
Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaint(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print("Erro! por favor, digite um número inteiro válido. ")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            break
        else:
            return n


def leiafloat(prompt):
    while True:
        try:
            n = float(input(prompt))
        except (ValueError, TypeError):
            print("Erro! por favor, digite um número inteiro válido. ")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            break
        else:
            return n

def main():
    n1 = leiaint("Digite um número inteiro: ")
    n2 = leiafloat("Digite um número real: ")
    print(f"O número inteiro digitado foi {n1} e o real {n2}.")


if __name__ == "__main__":
    main()
