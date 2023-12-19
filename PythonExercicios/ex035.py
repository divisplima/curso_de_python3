"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.
"""
side1 = int(input("Tamanho do reta 1: "))
side2 = int(input("Tamanho da reta 2: "))
side3 = int(input("Tamanho da reta 3: "))

if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2):
    print(f"As retas com comprimentos {side1}, {side2} e {side3} podem formar um triângulo.")
else:
    print(f"As retas com comprimentos {side1}, {side2} e {side3} não podem formar um triângulo.")
