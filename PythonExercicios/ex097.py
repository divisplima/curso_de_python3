"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.

Ex.: 'Olá, Mundo!'
Saída:
~~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~~
"""
def escreva(text):
    print("~" * (len(text) + 4))
    print(f"{text:^{len(text) + 4}}")
    print("~" * (len(text) + 4))


def main():
    escreva("Hello, World!")
    escreva("by lizlovelace")
    escreva("CURSO EM VÍDEO PYTHON")


if __name__ == "__main__":
    main()
