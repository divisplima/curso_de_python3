"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
comprar.
Considere US$1.00 = R$3.27
"""
print("=" * 40)
print(f"{'CONVERSOR DE MOEDAS':^40}")
print(f"{'BRL x USD':^40}")
print("=" * 40)

exchange_rate = 3.27
brl = float(input("Quanto deseja trocar? R$"))

usd = brl / exchange_rate
print(f"Você receberá US${usd:.2f}")
