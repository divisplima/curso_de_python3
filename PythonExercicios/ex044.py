"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:

- À vista dinheiro\cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros
"""
print("=" * 40)
print(f"{'CALCULADORA DE PREÇOS':^40}")
print("=" * 40)

price = float(input("Digite o preço do produto: R$"))

print("""Escolha a condição de pagamento:
[1] À vista dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)""")
option = int(input("Opção: "))

if option == 1:
    final_price = price * 0.9
elif option == 2:
    final_price = price * 0.95
elif option == 3:
    final_price = price
elif option == 4:
    final_price = price * 1.2
else:
    final_price = 0
    print("Opção inválida.")

print(f"O valor final do produto é: R${final_price:.2f}")
