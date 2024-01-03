"""
Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar um comando e o manual vai
aparecer. Quando o usuário digitar 'FIM', o programa se encerrará.

Obs.: Use cores.
"""
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def imprimir_texto_colorido(texto, cor):
    print(f"{cor}{texto}{Style.RESET_ALL}")

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", Fore.YELLOW)
    imprimir_texto_colorido("Help do comando:", Fore.CYAN)
    help(com)
    sleep(2)

def titulo(msg, cor=Fore.WHITE):
    tam = len(msg) + 4
    imprimir_texto_colorido("~" * tam, cor)
    imprimir_texto_colorido(f"  {msg}", cor)
    imprimir_texto_colorido("~" * tam, cor)
    sleep(1)

def main():
    comando = None

    while True:
        titulo("SISTEMA DE AJUDA PyHELP", Fore.GREEN)
        comando = input("Função ou biblioteca (ou 'FIM' para encerrar): ")

        if comando.upper() == "FIM":
            break
        else:
            ajuda(comando)
    
    titulo("ATÉ LOGO", Fore.RED)

if __name__ == "__main__":
    main()
