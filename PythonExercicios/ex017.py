"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
e mostre o comprimento da hipotenusa.
"""
from math import hypot

opposite_leg = float(input("Cateto oposto: "))
adjacent_leg = float(input("Cateto adjacente: "))
hypotenuse = hypot(opposite_leg, adjacent_leg)
# hypotenuse = (opposite_leg**2 + adjacent_leg**2) ** 0.5
print(f"A hipotenusa é {hypotenuse:.1f}.")
