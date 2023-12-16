"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
ângulo.
"""
from math import radians, sin, cos, tan

angle_in_degrees = float(input("Ângulo: "))
angle_in_radians = radians(angle_in_degrees)

sine = sin(angle_in_radians)
cosine = cos(angle_in_radians)
tangent = tan(angle_in_radians)

print(f"Seno: {sine:.2f}\nCosseno: {cosine:.2f}\nTangente {tangent:.2f}")
