"""
Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
de 2m^2.
"""
heigth = float(input("Altura (m): "))
width = float(input("Largura (m): "))

area = heigth * width
required_paint = area / 2

print(f"A área total da parede é de {area}m^2.")
print(f"Você precisará de {required_paint}L para pintar a parede.")
