"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição aparece a primeira vez.
- Em que posição ela aparece uma última vez.
"""

sentence = str(input("Insira uma frase qualquer: ")).strip().upper()
print(f"Aparece a letra 'A' {sentence.count('A')} vezes.")
print(f"Aparece a primeira vez na {sentence.find('A') + 1}ª posição.")
print(f"Aparece pela última vez na {sentence.rfind('A') + 1}ª posição.")
