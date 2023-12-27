"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
print("=" * 40)
print(f"{'TABUADA v.3.0':^40}")

while True:
    print("=" * 40)
    num = int(input("Insira um número para ver sua tabuada: "))

    if num < 0:
        break

    for i in range(10):
        print(f"{num} * {i+1:2} = {num * (i+1)}")
print("FIM DO PROGRAMA")
