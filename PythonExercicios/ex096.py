"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""
def title():
    print("=" * 40)
    print(f"{'CONTROLE DE TERRENOS':^40}")
    print("=" * 40)


def calcular_area(width, length):
    area = width * length
    print(f"A área de um terreno de {width}m x {length}m é {area}m^2.")


def main():
    title()
    
    width = float(input("Largura (m): "))
    length = float(input("Comprimento (m): "))
    
    calcular_area(width, length)


if __name__ == "__main__":
    main()
