"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
possíveis sobre ele.
"""
text = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(text)}")
print(f"É composto por espaços? {text.isspace()}")
print(f"É numérico? {text.isnumeric()}")
print(f"É alfabético? {text.isalpha()}")
print(f"É alfanumérico? {text.isalnum()}")
print(f"Está em maiúsculas? {text.isupper()}")
print(f"Está em minúsculas? {text.islower()}")
print(f"Está capitalizada? {text.istitle()}")
