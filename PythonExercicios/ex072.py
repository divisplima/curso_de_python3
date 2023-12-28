"""
Crie um programa que leia uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
numbers_in_words = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
                    "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze",
                    "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito",
                    "Dezenove", "Vinte")

number = None

while True:
    number = int(input("Digite um número de 0 a 20: "))

    if 0 <= number <= 20:
        break
    print("Tente novamente.", end=' ')
print(f"Você digitou o número {numbers_in_words[number]}.")
