"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples.

O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from time import sleep
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Inicializa o colorama para reset automático das cores

def leiaint(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (ValueError, TypeError):
            print(Fore.RED + "Erro! Por favor, digite um número inteiro válido.")
            continue
        except KeyboardInterrupt:
            print(Fore.RED + "Entrada de dados interrompida pelo usuário.")
            break
        else:
            return n


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(Fore.BLUE + txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")

    c = 1

    for i in lista:
        print(Fore.YELLOW + f"{c} - {i}")
        c += 1
    print(linha())

    opc = leiaint(Fore.MAGENTA + "Sua opção: ")
    return opc


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(Fore.RED + "Houve um erro na criação do arquivo")
    else:
        print(Fore.GREEN + f"Arquivo {nome} criado com sucesso")


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(Fore.RED + "Erro ao ler o arquivo.")
    else:
        cabecalho('PESSOAS CADASTRADAS')
        
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(Fore.CYAN + f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(Fore.RED + "Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')    
        except:
            print(Fore.RED + "Houve um erro na hora de escrever os dados.")
        else:
            print(Fore.GREEN + f"Novo registro de {nome} adicionado.")
            a.close()


def main():
    arq = 'PythonExercicios\ex115.txt'

    if not arqExiste(arq):
        criararquivo(arq)

    while True:
        resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

        match resposta:
            case 1:
                lerarquivo(arq)
            case 2:
                cabecalho("NOVO CADASTRO")

                nome = str(input(Fore.YELLOW + "Nome: ")).strip()
                idade = leiaint(Fore.YELLOW + "Idade: ")
                cadastrar(arq, nome, idade)
            case 3:
                print(Fore.RED + "Saindo do sistema...")
                break
            case _:
                print(Fore.RED + "Digite uma opção válida.")
        sleep(2)


if __name__ == "__main__":
    main()
