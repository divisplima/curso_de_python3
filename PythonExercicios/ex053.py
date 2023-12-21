"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.
Ex.: APOS A SOPA
     A SACADA DA CASA
     A TORRE DA DERROTA
     O LOBO AMA BOLO
     ANOTARAM A DATA DA MARATONA
"""
setence = str(input("Digite uma frase: ")).strip().replace(' ', '').upper()
reversed_setence = ''

for char in setence[::-1]:
    reversed_setence += char
print(f"A frase ao contrário: {reversed_setence}")

if setence == reversed_setence:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
